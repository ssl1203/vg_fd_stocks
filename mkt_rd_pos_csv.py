
import csv
import re
import traceback

def vanguard_reader(accounts_dict,csv_file_name):
    
    count_0 = 0
    count_line = 0

    pos_list = [[] for x in range(0)]

    try:
        csv_file  = open(csv_file_name)
        csv_reader = csv.reader(csv_file, delimiter=',')  
    except:
        print(f'**** Failed to open {csv_file_name}')
        exit(-1)
        return False
    
    for row in csv_reader:
        count_line+=1
        if (count_line==1):  # skip header line
            continue
        if len(row)==0 or row[0]=='':      # terminate if two consecutive null lines
            count_0+=1
            if (count_0>1):
                break 
            continue
        count_0=0        
        acc_name = accounts_dict.get(row[0],'undefined')
        if acc_name=='undefined':
            #print(f"OK z, Invalid account number {row[0]}")
            continue
        
        try :
            symb = row[2]
            shares = float(row[3])
            price = float(row[4])
            
            if int(price) == 1:
                symb = '$$CASH'
            pos_list.append([acc_name,symb,shares])
        except :
            print(f'*** Fatal Error (202) : Not able save {row}')
            return pos_list                         
    return pos_list


#convert currency string "$123,456.79" to floating point
def currency_to_float(currency_string,line_num):
    try:
        str = re.sub('[$,]', '', currency_string)
        return float(str)     
    except:
        traceback.print_exc()
        print(f'not able to convert currency_string [{currency_string}] string to float (352) line={line_num}')
        return 0




def fidelity_reader(accounts_dict,csv_file_name):

    fd_last_acc = ''
    pos_list = [[] for x in range(0)]
    try:
        count_0 = 0
        with open(csv_file_name) as csv_file:
            #print(f"File Opened : [{csv_file_name}]")
            fd_csv_reader = csv.reader(csv_file, delimiter=',')
            for fd_row in fd_csv_reader:
                count_0+=1
                if (count_0 ==1):  # skip the first line only
                    continue
                if len(fd_row)==0 or fd_row[0]=='':
                    break

                fd_acc_name = accounts_dict.get(fd_row[0],'undefined')
                if fd_acc_name== 'undefined' :
                    if (fd_row[0]!='X38745588'):
                        print(f"*** Warning (215) : account : ({fd_row[0]}  Sumb : ({fd_row[2]})) not processed")
                    continue

                if (fd_row[2]=='656568508'):
                    continue                         

                try :
                    if (fd_row[2]=='Pending Activity' or fd_row[2]=='SPAXX**' or fd_row[2]=='FDRXX**'):
                        shares = currency_to_float(fd_row[7],382)
                        pos_list.append([fd_acc_name,'$$CASH',shares])
                    else:
                        symb = fd_row[2]
                        price=0
                        share=0

                        try:
                            price = currency_to_float(fd_row[5],393)                             
                            shares = currency_to_float(fd_row[4],394)
                        except:
                            print('fatal error :',price,shares)
                            return pos_list
                            
                        #save_to_holding_pool(symb,shares,price,fd_acc_name,fd_row[0])
                        if int(price) == 1:
                            symb = '$$CASH' 
                        pos_list.append([fd_acc_name,symb,shares])
                except ValueError:
                    traceback.print_exc()
                    print(f'***Fatal Error (394) : add_shares symb={symb}, price={price} failed') 
                    return pos_list

    except:
        print(f'***Fatal Error (246) : Unable process [{csv_file_name}]') 
        exit(-1)
        return False
        

    return pos_list


##########################################################
# Read Taiwan CSV file into 2 D array
# { Symbol, Price, Total Value, Total Shares, yuanta, cathay, mega}
# 
#########################################################
def tw_reader2(cvs_file_name):
    fd_last_acc = ''
    pos_list = [[] for x in range(0)]
    try:
        with open(f"{cvs_file_name}") as csv_file:
            print(f"File Opened : [{cvs_file_name}2]")
            fd_csv_reader = csv.reader(csv_file, delimiter=',')
            count_0=0
            for row in fd_csv_reader:
                if len(row)==0 or row[0]=='':
                    break
                tw_acc_name = row[0]
 
                try :             
                    symb = row[1]
                    shares = float(row[2])
                    pos_list.append([tw_acc_name,symb,shares])
                    #print(f"++++++{tw_acc_name},   {symb},  {shares}" )
                                  
                except ValueError:
                    print('-------line 280', row[0],row[2])
                    traceback.print_exc()
                    print(f'***Fatal Error (815) : symb={symb} Failed to process ({cvs_file_name})') 
                    return pos_list

    except Exception as e:
        print(e)
        traceback.print_exc()
        print(f'***Fatal Error (246) : Unable to process ({cvs_file_name})') 

    return pos_list
###########################################################


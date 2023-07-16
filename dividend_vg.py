
import os
import platform
if (platform.system()=='Darwin'):
    g_data_path = f"{os.getcwd()}/data/" 
else: 
    g_data_path = f"C:\\Users\\seanl\\OneDrive\\80-股市\\00-Stock\\data\\"

print('\r\n\r\n')
print('****')
print(f'**** Make sure ({g_data_path}vg.csv)')
print(f'**** has all YTD transactions included')
print('****')
print('\r\n\r\n')
input('Press \'Enter\' key to continue: ')

file = open(f'{g_data_path}vg.csv','r')
#lines = f.readline()
count=-999999
total=0
mm_total = 0
for line in file:
    #print (x[0:8])
    tokens = line.split(',',20)
    if tokens[0]!='31141191':
        continue
    if len(tokens) > 5 and tokens[3]== 'Dividend':
        #print(tokens)
        price= round(float(tokens[9]),2)
        if tokens[6] == "":
            symb="VMFXX"
            mm_total += price
        else:
            symb=tokens[6]
        total += price     
        print(f'Date={tokens[1]},  Symb={symb},  Price={price} ')

print(f"MM Dividend = {mm_total}, All Dividend = {round(total,2)}")
   
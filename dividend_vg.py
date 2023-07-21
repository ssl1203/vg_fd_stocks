import os
import platform

from datetime import datetime

if (platform.system()=='Darwin'):
    g_data_path = f'{os.path.dirname(__file__)}/../vg_fd_stocks_data/'
else: 
    g_data_path = f"{os.getcwd()}\\..\\vg_fd_stocks_data\\" 



print('\r\n\r\n')
print('****')
print(f'**** Make sure ({g_data_path}vg.csv)')
print(f'**** has all YTD transactions included')
print('****')
print('\r\n\r\n')
input('Press \'Enter\' key to continue: ')

file = open(f'{g_data_path}vg.csv','r')
#lines = f.readline()

stock_sold = []
VMFXX_div = []
stock_div = []
count=-999999

for line in file:
    #print (x[0:8])
    tokens = line.split(',',20)
    if tokens[0]!='31141191' or len(tokens) < 8:
        continue

    date_object = datetime.strptime(tokens[1], '%Y-%m-%d').date()
    if date_object.year < 2023:
        continue
    
    if tokens[3]== 'Dividend':
        #print(tokens)
        price= round(float(tokens[9]),2)
    
        if tokens[6] == "":
            VMFXX_div.append([date_object.strftime('%Y-%m-%d'),"VMFXX",price])
        else:
            stock_div.append([date_object.strftime('%Y-%m-%d'),tokens[6],price])
                  
    elif tokens[3] == 'Sell':
        price= round(float(tokens[9]),2)
        stock_sold.append([date_object.strftime('%Y-%m-%d'),tokens[6],price])
    else:
        continue


total = 0
stock_div_total = 0
VMFXX_total = 0 
for div in VMFXX_div:
    print(f'** {div[0]}, {div[1]}, {div[2]}')
    VMFXX_total+=div[2]

print(f' VMFXX sub total = {VMFXX_total}')
print('-----------------------------')

for div in stock_div:
    print(f'** {div[0]}, {div[1]}, {div[2]}')
    stock_div_total+=div[2]

print(f' Stock dividend total = {stock_div_total}')
print('-----------------------------')
stock_sold_total = 0
for tokens in stock_sold:
    stock_sold_total+=tokens[2]
    print(f'** {tokens[0]}, {tokens[1]}, {tokens[2]}')

print('-----------------------------')

print(f"VMFXX = {round(VMFXX_total,2)}, Stock Div = {round(stock_div_total,2)}, Stock Sell ={round(stock_sold_total,2)}")
print(f' TOTAL = {round(VMFXX_total+stock_div_total+stock_sold_total,2)}')   



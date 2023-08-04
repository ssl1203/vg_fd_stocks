#--------------- instrcution -----------------
# 1. Display saving account 'activities' from Fidelity web page
# 2. Select relevent text on the web page and Copy
# 3. Paste to Notepad++ and save as txt file for input 

# ------------ File format ----------------------
# The each dividend transaction consists of many consecutive lines it starts with --
#   'Date' , 'DIVIDEND'+symbol followed by 'Price', others are ignored
#
# ------------File input example------------
#Jun-30-2023	
#DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)	
#+$215.92
#$55,873.20	
#Show details
#
#

import re
from datetime import datetime
import os
import platform
if (platform.system()=='Darwin'):
    g_data_path = f'{os.path.dirname(__file__)}/../vg_fd_stocks_data/'
else: 
    g_data_path = f"{os.getcwd()}\\..\\vg_fd_stocks_data\\" 


file = open(f'{g_data_path}fd_div_ytd.txt','r')

total=0
total2=0
found_div = False
date_last = datetime.today
for line in file:
    if (len(line)>11) :
        try: 
            date_try = datetime.strptime(line[0:11], '%b-%d-%Y').date()
            date_last = date_try
            continue
        except:
            ii=0 #do nothing

    if line[0:8] == 'DIVIDEND':
        found_div = True     
        m = re.findall('\([\w]+', line) 
        
        if len(m) < 2:
            print('*********** parse error ',line)
            continue
        symb_last = m[0][1:]
        continue

    if found_div :
        m2 = re.findall('[0-9\.]+', line) 
        total2+= float(m2[0])
        dividend = float(line[2:])
        total+=dividend
        print('Date : ', date_last, ' Symbol :', symb_last, ', Dividend :',dividend)
    found_div = False
        

print(f"All Dividend = {round(total,2)}", 'Total2=',total2)
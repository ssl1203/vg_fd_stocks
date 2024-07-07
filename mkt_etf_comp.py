from bs4 import BeautifulSoup
import requests
import lxml


#get the percentage of ETF component stocks
def get_etf_components(ETF):
    url = f'https://www.schwab.wallst.com/schwab/Prospect/research/etfs/schwabETF/index.asp?type=holdings&symbol={ETF}'
    etf_html = requests.get(url)
    soup = BeautifulSoup(etf_html.content, 'html.parser')
    
    holding_dict = {} 
    found = False
    # Find all 'div' elements with the 'entry-content' class and extract text
    for item in soup.find_all('table', { 'class' : 'standard sortable'}):   
        found = True
        first = True
        for stock in item.find_all('tr'): 
            symb = ''
            percent = ''
            for idx,elem in enumerate(stock.find_all('td')):             
                if idx==0:
                    #print(f'====={stock_rank}=====')
                    #print("Symbol :",elem.text)
                    symb = elem.text
                    #lines[stock_rank] = lines[stock_rank] + f'   {elem.text}  '
                if  idx==2:
                    percent = elem.text
                    #print("Price :",elem.text)
                    #lines[stock_rank] = lines[stock_rank] + f'   {elem.text}  #'

            if symb == '':
                continue
            holding_dict[f'{symb}'] = float(percent.replace('%',''))  
            
    return holding_dict      


#yahoo_fin
#http://theautomatic.net/2018/07/31/how-to-get-live-stock-prices-with-python/
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/about-me/
from yahoo_fin import stock_info as si
import pandas as pd
import yfinance as yf # backup for mutual fund

def get_current_stock_price(symb):

    if symb == 'USD=X' or symb=='CASH' or symb=='$$CASH':
        return 1
    
    price = si.get_live_price(symb) 

    #get last close price if live_price not available 
    if pd.isna(price) :
        try:
            stock_info = yf.Ticker(symb)
            data = stock_info.history(period="1wk") # '1mo' '20mo' 
            prices = data['Close']
            price = prices.iloc[-1]
            #print(f'OK 5,  Got last close : {symb}')
        except:
            price=0
    return round(price ,2)   
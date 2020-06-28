import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd


#Symbol = 'SPY AMZN TSLA'
selected_symbol = input("Please input stock symbols, i.e. 'SPY AMZN TSLA' : " )


#StockData = yf.Tickers(Symbol)
StockData = yf.Tickers(selected_symbol)
today = datetime.datetime.today().isoformat()

#StockPrices = StockData.history(period='1d', start='2010-1-1', end='2020-2-10')
StockPrices = StockData.history(period='1d', start='2001-1-1', end=today[:10])

#print(type(StockPrices['Close'].head()))

sph = StockPrices['Close'].head()
#print(sph)
if str(sph.isnull().values.any()) == "True":
    print("Sorry, please enter a proper range of time")
    exit()





ClosePrices = StockPrices['Close']
stock_return = ClosePrices.apply(lambda x: x / x[0])
#print(stock_return.head())



#StockPrices['Close'].plot(grid=True)
stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)


#plt.show(block=False)


#plt.show()

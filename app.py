import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd


#Symbol = 'SPY AMZN TSLA'
while True:
    selected_symbol = input("Please input two or more stock symbols, i.e. 'SPY AMZN TSLA' : " )
    try:
        StockData = yf.Tickers(selected_symbol)
        sp = StockData.history()
        break
    except KeyError:
        print("Please enter valid symbols")
    except ValueError:
        print("Please input stock symbols")
        



#StockData = yf.Tickers(Symbol)

#today = datetime.datetime.today().isoformat()[:10]

while True:
    startdate = input("Please enter the start date in this format '2001-1-1' : " )
    if not startdate:
        print("no input start date")
    enddate = input("Please enter the end date in this format '2001-1-1' : " )
    if not enddate:
        print("no input end date")
    try:
        datetime.datetime.strptime(startdate, "%Y-%m-%d")
        datetime.datetime.strptime(enddate, "%Y-%m-%d")
    except ValueError:
        print("Wrong format")
    else:
        StockPrices = StockData.history(period='1d', start=startdate, end=enddate)
        ClosePrices = StockPrices['Close']
        if str(ClosePrices.isnull().values.any()) == "True":
            print("Sorry, please enter a proper time range for the selected stock symbols")
        elif not startdate:
            print("no input start date")
        elif not enddate:
            print("no input end date")   
        else:
            break

#StockPrices = StockData.history(period='1d', start='2010-1-1', end='2020-2-10')
#StockPrices = StockData.history(period='1d', start=startdate, end=today)

#print(type(StockPrices['Close'].head()))




ClosePrices.plot()
plt.title("Stocks Historical Prices(Daily)")


stock_return = ClosePrices.apply(lambda x: x / x[0])
#print(stock_return.head())

stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
plt.title("Stocks Return Comparison")


#plt.show(block=False)
#plt.show()

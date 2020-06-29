import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd

print("-------------------------")
#Symbol = 'SPY AMZN TSLA'
while True:
    selected_symbol = input("Please input two or more stock symbols. Each symbol must be separated by one single space, e.g. 'SPY AMZN TSLA': " )
    try:
        StockData = yf.Tickers(selected_symbol)
        sdh = StockData.history()
        break
    except KeyError:
        print("Please enter at least two valid stock symbols")
    except ValueError:
        print("Please input some stock symbols")
        
#today = datetime.datetime.today().isoformat()[:10]

while True:
    startdate = input("Please enter the start date in this format '2001-1-1' : " )
    if not startdate:
        print("no input start date")
    else:
        try:
            datetime.datetime.strptime(startdate, "%Y-%m-%d")
        except ValueError:
            print("Incorrect start date format")
        else:
            while True:
                enddate = input("Please enter the end date in this format '2001-1-1' : " )
                if not enddate:
                    print("no input end date")
                else:
                    try:
                        datetime.datetime.strptime(enddate, "%Y-%m-%d")
                    except ValueError:
                        print("Incorrect end date format")
                    else:
                        break
            StockPrices = StockData.history(period='1d', start=startdate, end=enddate)
            ClosePrices = StockPrices['Close']
            if str(ClosePrices.isnull().values.any()) == "True":#check if there's any NaN value which means the stock price is not available at this time/date
                print("Sorry, please enter a proper time range for the selected stock symbols") 
            else:
                break

#StockPrices = StockData.history(period='1d', start='2010-1-1', end='2020-2-10')
#StockPrices = StockData.history(period='1d', start=startdate, end=today)

#print(type(StockPrices['Close'].head()))




ClosePrices.plot()
plt.title("Stocks Historical Prices(Daily)")


stock_return = ClosePrices.apply(lambda x: x / x[0])
#print(type(stock_return.tail(1)))
last_return = stock_return.tail(1)
#print(last_return.idxmax(axis = 1))
#print(type(last_return.idxmax(axis = 1)))
#print(last_return.idxmax(axis = 1).get)
print(last_return.idxmax(axis = 1).values)



stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
plt.title("Stocks Return Comparison")


#plt.show(block=False)
#plt.show()



###
#  save plots
#  create reports 

#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#
#rank = 1
#for d in top_sellers:
#    print("  " + str(rank) + ") " +
#          d["name"] + ": " + to_usd(d["monthly_sales"]))
#    rank = rank + 1
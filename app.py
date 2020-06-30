import yfinance as yf
import matplotlib.pyplot as plt
import datetime
from yfinance import multi, shared#for one type of error below: 'shared._ERRORS'

print("-------------------------")
print("   STOCKS GRAPHING APP   ")
print("-------------------------")

today = datetime.datetime.today().isoformat()[:10]
print("Date: ", today)
print("-------------------------")

##User input

while True:
    selected_symbol = input("Please input two or more stock symbols. Each symbol must be separated by one single space, e.g. 'SPY AMZN TSLA': " )
    try:
        StockData = yf.Tickers(selected_symbol)
        sdh = StockData.history()#to test if the results are valid
        if shared._ERRORS:#if one or more symbol is misspelled
            print("Please check the spellings and try again")
        else:
            break
    except (KeyError, AttributeError):#if input only one symbol or non-letter input 
        print("Please enter at least two valid stock symbols")
    except ValueError:#if input nothing 
        print("Please input some stock symbols")
       

while True:
    startdate = input("Please enter the start date in this format '2001-01-01': " )
    if not startdate:
        print("Missing start date input")
    else:
        try:
            datetime.datetime.strptime(startdate, "%Y-%m-%d")
        except ValueError:
            print("Incorrect start date format")
        else:
            while True:
                enddate = input("Please enter the end date in this format '2001-01-01': " )
                if not enddate:
                    print("Missing end date input")
                else:
                    try:
                        datetime.datetime.strptime(enddate, "%Y-%m-%d")
                        if enddate > today:
                            print("The end date must be set ealier than or on today's date: ",today)
                        else:
                            break
                    except ValueError:
                        print("Incorrect end date format")                        
            StockPrices = StockData.history(period='1d', start=startdate, end=enddate)
            ClosePrices = StockPrices['Close']
            if str(ClosePrices.isnull().values.any()) == "True":#check if there's any NaN value which means the stock price is not available at this time/date
                print("Sorry, please enter a proper time range for the selected stock symbols") 
            else:
                break


##Graphing

ClosePrices.plot(grid = True)
plt.title("Stocks Historical Prices (Daily)")
plt.savefig('graphs/Stocks Historical Prices.png')


stock_return = ClosePrices.apply(lambda x: x / x[0])


stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
plt.title("Stocks Return Comparison")
plt.savefig('graphs/Stocks Return Comparison.png')


##Output Report

last_trading_date = str(stock_return.index[-1])[:10]

last_return = stock_return.tail(1)

ranking = last_return.T.rank(ascending = False).astype(int)

sorted_rank = ranking.sort_values(by=[last_trading_date])

growth_rates = last_return.T.values.tolist()#Transpose the matrix to set the growth rate as a tow and list the values, which creates a nested list
list_of_return = []
for list in growth_rates:
    for x in list:
        list_of_return.append(x)#turn the nested list into a simple list
        
sorted_returns = (sorted(list_of_return, reverse=True))

rates_of_return = ["{:.2%}".format(y-1) for y in sorted_returns]

output_report = sorted_rank.assign(empty=' ' * len(sorted_rank.index), Returns=rates_of_return)#add the rates of return as a column and an empty column with a single space for alignment in the report


print("-------------------------")
print("Output graphs saved to the 'graphs' folder in this directory")
print("-------------------------")
print("-------------------------")
print("Stock Returns Ranking Report")
print("                         ")
print("Start Date: ", str(datetime.datetime.strptime(startdate, "%Y-%m-%d"))[:10])
print("End Date:   ", str(datetime.datetime.strptime(enddate, "%Y-%m-%d"))[:10])
print("                         ")
print("Stock|Rank|Rate of Return")
print(output_report.to_string(header=False))
print("-------------------------")
print("-------------------------")
print("Thank you for using the stocks graphing app.")
print("-------------------------")


##Showing Graphs

#plt.show(block=False)
plt.show()


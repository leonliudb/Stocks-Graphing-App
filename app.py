import yfinance as yf
import matplotlib.pyplot as plt

Symbol = 'AMZN TSLA'

StockData = yf.Tickers(Symbol)

StockPrices = StockData.history(period='1d', start='2017-1-1', end='2020-2-10')

#print(StockPrices)
#print(StockPrices['Close'].head())
ClosePrices = StockPrices['Close']
stock_return = ClosePrices.apply(lambda x: x / x[0])
#print(stock_return.head())


#StockPrices['Close'].plot(grid=True)
stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
plt.show()

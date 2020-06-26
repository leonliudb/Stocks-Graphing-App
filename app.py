import yfinance as yf
import matplotlib.pyplot as plt

Symbol = 'AMZN TSLA'

StockData = yf.Tickers(Symbol)

StockPrices = StockData.history(period='1d', start='2020-1-1', end='2020-1-10')

print(StockPrices)



StockPrices['Close'].plot(grid=True)

plt.show()

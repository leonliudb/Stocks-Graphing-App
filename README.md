# Stock-Graphing-App

This is a stocks' return and prices graphing application in Python.
Uses Yahoo! Finance market data downloader(https://pypi.org/project/yfinance/) to retrive stock data and the rate of return over a certain user-defined time frame.



## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Clone or download [this repository](https://github.com/leonliudb/Stocks-Graphing-App) onto your computer. Then navigate there from the command line:

```sh
cd Stocks-Graphing-App
```

## Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n stocksgraph-env python=3.7 # (first time only)
conda activate stocksgraph-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

```sh
pip install -r requirements.txt
```

## Usage

Run the recommendation script:

```py
python app.py
```

Example output:

![example](https://github.com/leonliudb/Stocks-Graphing-App/blob/master/sample%20graphs/Stocks%20Historical%20Prices.png)


## [License](/LICENSE.md)






import pandas as pd
from pandas import DataFrame
from pandas_datareader import data, wb

import datetime

sp500 = data.get_data_yahoo('%5EGSPC',start = datetime.datetime(2009, 10, 1), end = datetime.datetime(2010, 10, 1))
print(sp500.head())
sp500.to_csv('sp500_ohlc.csv')
df = pd.read_csv('sp500_ohlc.csv')
print('Before: \n', df)  # Adds extra column with serial numbers
df = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates=True)
print('After: \n', df)
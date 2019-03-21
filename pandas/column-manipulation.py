
import pandas as pd
from pandas import DataFrame
from pandas_datareader import data, wb
import datetime

df1 = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates=True)
print('DF1 Sample Data: \n', df1.head())

df2 = df1['Open']
print('DF2 Sample Data: \n', df2.head())

df3 = df1[['Open', 'Close', 'Volume']]  # Note the two brackets like list of a list
print('DF3 Sample Data: \n', df3.head())

del df3['Volume']
print('DF3 Data - Post Del: ', df3.head())
print('-------------------------------------------')

df4 = df1[['Open', 'Close', 'Volume']]
df4.is_copy=False
df4.rename(columns={'Close': 'CLOSE'}, inplace=True)
print('Revised DF4 Data: ', df4.head())

df5 = df1[(df1['Close'] > 500)]
print(df5)

# Referencing keys and values in df

df1['H-L'] = df1['High'] - df1.Low
print("Moving Avg", df1.head())

# df1['100MA'] = df1.rolling(window=).mean()
# print("Rolling 100 AVG", df1[200:210])

df1['Difference'] = df1['Close'].diff()


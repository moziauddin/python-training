import pandas as pd

# Shift is available for both time series and dataframe
# The below is to shift the values keeping dates constant
df1 = pd.read_csv('files/prices.csv', index_col='Date', parse_dates=True)
print(df1.shift(1))
df1['Prev Day Price'] = df1['Price'].shift(1)
df1.fillna(0, inplace=True)
df1['Price Diff'] = df1['Price'] - df1['Prev Day Price']
df1['5D% gain'] = (df1['Price']-df1['Price'].shift(5))*100 / df1['Price'].shift(5)
df1.fillna(0, inplace=True)
print(df1)

# To shift dates keeping values constant

df2 = pd.read_csv('files/prices.csv', index_col='Date', parse_dates=True)
print(df2.index)
df2.index = pd.date_range(start='1/22/2019', end='2/5/2019', freq='B')
print(df2.tshift(1))
# Use the below functions to fill missing data
# fillna
# dropna
# interpolate

import pandas as pd


df1 = pd.read_csv('files/miss-data.csv', parse_dates=['Date'])
print(df1)
print(type(df1['Date'][0]))

# Make date column an index

df1.set_index('Date', inplace=True)
print(df1.head())

# Replace NaN values with alternate values
df2 = df1.fillna(0)
print(df2)
# Relace each column with a different value for NA
df3 = df1.fillna({'JAN': 0, 'FEB': '-'})
print(df3)

# Use FFILL and BFILL to copy values from top to bottom and bottom to top
df4 = df1.fillna(method='ffill')
print(df4)

df5 = df1.fillna(method='bfill')
print(df5)

# Use axis=column, you can copy values across columns using fillna

df6 = df1.fillna(method='bfill', axis='columns')
print(df6)

# Limits the copying to a certain number of times
df7 = df1.fillna(method='ffill', limit=1)
print(df7)

# To interpolate in linear fashion, use interpolate

df8 = df1.interpolate(method='linear')
print(df8)

df9 = df1.interpolate(method='time')
print(df9)

# Drop rows with NaN values
df10 = df1.dropna()
print(df10)

# To build a DF with missing dates in the index
dt = pd.date_range('2014-02-28', '2019-02-02')
ind = pd.DatetimeIndex(dt)
df11 = df1.reindex(ind)
print('Date Time Index\n', df11)
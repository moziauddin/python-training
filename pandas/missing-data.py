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

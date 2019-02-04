import pandas as pd
import matplotlib


df1 = pd.read_csv('files/stocks.csv', parse_dates=['Date'], index_col='Date')
# Return data for a date
print(df1['2019-01-31'])
# Return data for a month
print(df1['2019-01'])
# Return the mean of close price for the month
print(df1['2019-01'].Close.mean())
print(df1['Open'])

#Resample for a monthly data for a specific column
print(df1.Open.resample('m').mean().plot())
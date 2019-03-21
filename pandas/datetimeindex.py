import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

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

df2 = pd.read_csv('files/stocks-appl.csv')
print(df2.head(3))

date_range = pd.date_range(end='24/1/2019', start='1/3/2019', freq='B')[::-1]  # [::-1] is slicing pattern
print(date_range)
date_range2 = pd.date_range(end='24/1/2019', periods=10, freq='B')[::-1]
print('Date Range2: \n', date_range2)
# Add index using set_index to data frame
df2.set_index(date_range, inplace=True)  # Add
print(df2)
# print(len(date_range))

plot = df2.Close.plot()  # Returns the full data set
plot1 = df2['20/1/2019':'24/1/2019'].Close.mean()
print(plot1)
plt.show()

# Genrate random data; Dates with some random numbers
import numpy as np
ts = pd.Series(np.random.randint(1,10,len(date_range2)), index=date_range2)
print(ts)
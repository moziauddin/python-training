import pandas as pd
import numpy as np

y1 = pd.Period('2016')
print(dir(y1))

print(y1.is_leap_year)
print(y1.start_time)
print(y1.end_time)

y2 = pd.Period('2019-1', 'M')
print(y2.freq)
print(y2.start_time, y2.end_time)
print(y2-10)  # Prints -10 days from y2

h1 = pd.Period('2019-2-6 14:00:00', 'H')
print(h1+pd.offsets.Hour(6))
print(h1 - 4)

q1 = pd.Period('2019-10', freq='Q-JAN')
print(q1)
print(q1.asfreq('M', how='end')-1)  # should print 2019-09

q2 = pd.Period('2018Q2', freq='Q-JAN')
print(q1-q2)  # Both frequencies need to be same freqeuncy

p_range = pd.period_range('2010', '2019', freq='Q')  # Also use periods
print('P_RANGE:\n', p_range)
print('LEN P_RANGE:', len(p_range))
print('P_RANGE idx 0', p_range[0])

print(p_range[1:5])
print(p_range[1:5].to_timestamp())  # Convert to timestamp
print(p_range[1:5].to_timestamp().to_period())  # Convert to Period


# Create a calendar with FY ending in Jan
df1 = pd.read_csv('files/company-profile.csv', index_col='Item')
df1 = df1.T
print('DF1 Index', df1.index)
df1.index = pd.PeriodIndex(df1.index, freq='Q-JAN')
print(df1.index)
df1['Start Date'] = df1.index.map(lambda x: x.start_time)  # map is to call a function and lambda for an inline function
df1['End Date'] = df1.index.map(lambda x: x.end_time)
print(df1)
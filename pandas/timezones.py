import pandas as pd
from pytz import all_timezones


# There are two types of time zones.
# pytz and dateutil

df1 = pd.read_csv('files/stocks.csv', index_col='Date', parse_dates=True)
print(df1)

print('Index Column: \n', df1.index)
df1 = df1.tz_localize(tz='Australia/Sydney')
print('Index Column: \n', df1.index)

df2 = df1.tz_convert(tz='Asia/Calcutta')  # Convert to Indian timezone
print(df2)


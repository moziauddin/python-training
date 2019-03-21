import pandas as pd


# PIVOT
df1 = pd.read_csv('files/city-weather.csv')
print(df1)

df2 = df1.pivot(index='Date', columns='City')
print(df2)  # Displays full pivot table

df2 = df1.pivot(index='Date', columns='City', values=['Forecast', 'Wind'])
print(df2)  # Displays full pivot table

# PIVOT TABLE
df3 = pd.read_csv('files/city-weather-same-day.csv', parse_dates=True)  # Parse dates does not work for some reason
print(df3)
df4 = df3.pivot_table(index='Date', columns='City')
print(df4)  # Prints average for the day as default

df4 = df3.pivot_table(index='Date', columns='City', aggfunc='count')
print(df4)  # Prints aggregate based on the function

df4 = df3.pivot_table(index='Date', columns='City', aggfunc='max', margins=True)
print(df4)  # Prints aggregate with all column

# Grouping
print(type(df3['Date'][0]))  # Date column is read as a string
df3['Date'] = pd.to_datetime(df3['Date'])  # Converted to date using the pd.to_datetime() func
# This beloe statement will fail without the date conversion
df5 = df3.pivot_table(index=pd.Grouper(freq='m', key='Date'), columns='City')
print(df5)
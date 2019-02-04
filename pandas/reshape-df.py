import pandas as pd


df1 = pd.read_csv('files/daily-weather.csv')
print(df1)

# Melt a dataframe
df2 = pd.melt(df1, id_vars=['day'])
print(df2)

# Print a specific column
print('Variable is \n\n', df2[df2['variable']=='canberra'])

# Print with proper column names using arguments to melt()
df2 = pd.melt(df1, id_vars=['day'], var_name='city', value_name='temparature')
print(df2)
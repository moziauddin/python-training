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

# Stack and Unstack Dataframe

df3 = pd.read_excel('files/comp-data.xlsx', sheet='comp-data', header=[0,1])
print(df3)

print(df3.stack())
print(df3.stack(level=0))  # level = 1 will transpose the company row

# If you have a stacked table you can unstack the same
print('S U L0', df3.stack().unstack(level=0))  # Same as Stack Unstack
print('S U L1', df3.stack().unstack(level=1))
print('Stack Unstack', df3.stack().unstack())  # Same as L0

import pandas as pd

df1 = pd.read_csv('files/sample.csv')
print(df1)
print(df1.columns)
print('Two Feb Values1\n', df1.FEB.head(2))
print('Two Feb Values2\n', df1['FEB'].head(2))
print(df1['FEB'].min())
print('Mean of Dec', df1.DEC.mean())
print('Dec STD', df1.DEC.std())

print(df1[2:4])  # Print specific Rows
print(df1[['City Name','JAN']])  # Put column names in a list

print(df1.describe())  # Print statistics

# Conditionally select data
print(df1[['City Name','JAN']][df1['JAN']>=50])  # Select city name and month where the month had value greater than 50
print(df1['City Name'][df1['FEB'] == df1['FEB'].max()])  # Prints City name where the temp is max temparature
print('Index: ', df1.index)

df1.set_index('City Name', inplace=True)
print(df1.head())
df1.reset_index(inplace=True)
print(df1.head())

# we can create datafames using the below five methods
# Dictionaries
# Lists
# Tuples
# CSV files
# Excel Files

sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
df2 = pd.DataFrame(sales)
print(type(sales))
print('DF from Dictionary: \n', df2)

df3 = pd.read_csv('files/sample.csv', skiprows=1)
print(df3.head(2))  # Skips the header row

df4 = pd.read_csv('files/sample.csv', header=None)
print(df4.head(2))  # Adds column index as well

df5 = pd.read_csv('files/sample.csv', nrows=3)
print(df5)  # Only reads three rows

df6 = pd.read_csv('files/sample.csv', nrows=3, na_values=6.0)
print(df6)  # Only reads three rows

df7 = pd.read_csv('files/sample.csv', nrows=3, na_values={
    'JAN': [16.0],
    'FEB': [6]
})
print(df7)  # Only reads three rows
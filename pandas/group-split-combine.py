import pandas as pd


df1 = pd.read_csv('files/city-weather.csv', index_col='Date', parse_dates=True)
# Create a Grouping by city
grp = df1.groupby('City')
print(grp.any())
print(type(grp))

# Print the grouping dataframe
for city, city_df in grp:
    print('City: - ', city, '\nCity Dataframe: - \n', city_df)

# Get a certain group
print(grp.get_group('Sydney'))

# Print max for all temp for all cities
print(grp.max())

print(grp.mean())
print(grp.describe())
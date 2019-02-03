import pandas as pd


aus_weather = pd.DataFrame({
    'city': ['Brissie', 'Sydney', 'Canberra'],
    'temp': [55, 32, 16],
    'wind': [66,50,80]
})

print(aus_weather)

us_weather = pd.DataFrame({
    'city': ['Boston', 'Califonia', 'Dallas'],
    'temp': [20, 33, 46],
    'wind': [90,32,36]
})

print(us_weather)

# Join DF together

all_cities = pd.concat([aus_weather, us_weather], ignore_index=True)
print(all_cities)

all_cities = pd.concat([aus_weather, us_weather], keys=['Aus', 'US'])
print(all_cities)
print(all_cities.loc['US'])

temp_df = pd.DataFrame({
    'city': ['Syd', 'Can', 'Mel'],
    'temp': [20,30,40]
})

wind_df = pd.DataFrame({
    'city': ['Syd', 'Can', 'Mel'],
    'wind': [70,80,90]
})

df2 = pd.concat([temp_df, wind_df])
print(df2)

'''
This prints below incorrectly
  city  temp  wind
0  Syd  20.0   NaN
1  Can  30.0   NaN
2  Mel  40.0   NaN
0  Syd   NaN  70.0
1  Can   NaN  80.0
2  Mel   NaN  90.0
'''

df2 = pd.concat([temp_df, wind_df], axis=1)
print(df2)
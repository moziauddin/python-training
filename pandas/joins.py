import pandas as pd


temp = pd.DataFrame({
    'city': ['Brissie', 'Sydney', 'Canberra'],
    'temp': [55, 32, 16]
})

hum = pd.DataFrame({
    'city': ['Brissie', 'Sydney', 'Canberra'],
    'hum': [23, 60, 17]
})

print(temp, 2*'\n', hum)

# Joining both dataframes to form one table

df1 = pd.merge(temp, hum, on='city')
print(df1)

temp1 = pd.DataFrame({
    'city': ['Brissie', 'Sydney', 'Canberra', 'Hobart'],
    'temp': [55, 32, 16, 8]
})

hum1 = pd.DataFrame({
    'city': ['Brissie', 'Sydney', 'Melbourne'],
    'hum': [23, 60, 12]
})

df2 = pd.merge(temp1, hum1, on='city')
print(df2)  # Prints only intersection (Inner-Join)

df2 = pd.merge(temp1, hum1, on='city', how='outer', indicator=True)
print(df2)  # Outer join (Union)

df2 = pd.merge(temp1, hum1, on='city', how='left')
print(df2)  # Left Join - includes the left plus intersection

df2 = pd.merge(temp1, hum1, on='city', how='right')
print(df2)  # Right Join - includes the right plus intersection

# Repeated columns for same cities
df3 = pd.DataFrame({
    'city': ['Syd', 'Mel', 'Bri'],
    'temp': [30, 30, 31],
    'hum': [60, 25, 35]
})

df4 = pd.DataFrame({
    'city': ['Syd', 'Mel', 'Can'],
    'temp': [30, 30, 45],
    'hum': [60, 25, 33]
})

df5 = pd.merge(df3, df4, on='city')
print(df5)

# Add our own suffices
df5 = pd.merge(df3, df4, on='city', how='outer', suffixes=['_left', '_right'])
print(df5)
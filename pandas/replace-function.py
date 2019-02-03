import pandas as pd
import numpy as np


df1 = pd.read_csv('files/replace.csv')
print('DF1:\n', df1)

# Replace using a list of values in the entire DF
df2 = df1.replace([-9999, -8888], np.NaN)
print('DF2:\n', df2)

# Replace using a list of values in a dictionary
df3 = df1.replace({
    'temparature': [-9999, -8888],
    'wind': 112,
     'event': ['0', '-']
   }, np.NaN)
print('DF3:\n', df3)

# Replace using a map across the dataframe
df4 = df1.replace({
    -9999: np.NaN,
    112: np.NaN,
    '-': 'No Event',
    '0': 'No Event'
})
print('DF4:\n', df4)

# Replace using a regular expression only in temp and wind columns
df5 = df1.replace('[A-Za-z]', '', regex=True)  # Replaces all characters inc event row
print('DF5:\n', df5)

df5 = df1.replace({
    'temparature': '[A-Za-z]',
    'wind': '[A-Za-z]'
}, '', regex=True)  # Using a disctionary
print('DF5 Again:\n', df5)

df6 = pd.read_csv('files/students.csv')
print('DF8:\n', df6)
print(df6.replace(['Exceptional', 'Great', 'Average', 'Poor', 'Hopeless'], [10,5,4,3,2]))
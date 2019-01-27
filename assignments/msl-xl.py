import pandas as pd
import csv


df1 = pd.read_excel('ICTV Master Species List 2018a v1.xlsx', '2018av1', index_col=0, dtype={'Realm': str, 'Subrealm': str, 'Kingdom': str, 'Subkingdom': str, 'Subclass': str})
# df.info()
print(df1.index)
print('Axes:', df1.axes)
print('Dimensions:', df1.ndim)
print('Size:', df1.size)
print('Shape:', df1.shape)
# print(df['Species'])
header_row = df1.columns.values
print(header_row)
print(df1.index.values)

data_set = []

for col_name in header_row:
    for item in df1[col_name].unique():
        lt = [item, col_name]
        data_set.append(lt)
with open('temp.csv', 'w', newline='') as out1:
    wr1 = csv.writer(out1)
    header = ['Name','Rank']
    wr1.writerow(header)
    wr1.writerows(data_set)

df2 = pd.read_csv('temp.csv')
print(df2)
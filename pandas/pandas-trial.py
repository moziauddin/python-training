import pandas as pd
import matplotlib
import matplotlib.pyplot as p
from mpl_toolkits.mplot3d import Axes3D
from pandas import DataFrame
from pandas_datareader import data, wb
import datetime

df1 = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates=True)
df1['H-L'] = df1['High'] - df1.Low
df1['Difference'] = df1['Close'].diff()
print('DF1 Sample Data: \n', df1.head())
df1.plot()
p.show()

df1[['Close', 'Volume']].plot()
p.show()

threed = p.figure().gca(projection='3d')
threed.scatter(df1.index, df1['H-L'], df1['Close'])
threed.set_xlabel('Index')
threed.set_ylabel('H-L')
threed.set_zlabel('Close')
p.show()
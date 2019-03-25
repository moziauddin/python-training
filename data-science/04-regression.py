import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

randData = np.random.normal(10,1,1000)
linData = 100 - (randData + np.random.normal(0,0.1,1000)) * 3

plt.scatter(randData, linData)
# plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(randData, linData)

print('R_Squared:', r_value ** 2)

def plot_line(x):
    return slope * x + intercept

line_lin = plot_line(randData)
plt.scatter(randData, linData)
plt.plot(randData, line_lin, c='b')
plt.show()

# Polynomial Regression
np.random.seed(2)
randData1 = np.random.normal(3,1,1000)
pol_data = np.random.normal(50, 10, 1000) / randData1
plt.scatter(randData1, pol_data)
plt.show()

x = np.array(randData1)
y = np.array(pol_data)
p4 = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
plt.scatter(x,y)
plt.plot(xp, p4(xp), c='r')
plt.show()

r2 = r2_score(y, p4(x))
print(r2)

# Multivariant Regression

df = pd.read_csv('mv-regression.csv')
print(df.head())

scale = StandardScaler()

X = df[['mpg', 'cyl', 'hp']]
Y = df['qsec']
X[['mpg', 'cyl', 'hp']] = scale.fit_transform(X[['mpg', 'cyl', 'hp']].as_matrix())
print(X)

est = sm.OLS(Y, X).fit()
print(est.summary())

print(Y.groupby(df.cyl).mean())

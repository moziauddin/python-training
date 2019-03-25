import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

randData = np.random.normal(10,1,1000)
linData = 100 - (randData + np.random.normal(0,0.1,1000)) * 3

plt.scatter(randData, linData)
# plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(randData, linData)

print(r_value ** 2)

def plot_line(x):
    return slope * x + intercept

line_lin = plot_line(randData)
plt.scatter(randData, linData)
plt.plot(randData, line_lin, c='y')
plt.show()
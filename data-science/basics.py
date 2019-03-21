import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import expon
from pylab import *

near = 200
std_dev = 40
num_dp = 10000
salaries = np.random.normal(near, std_dev, num_dp)

print("List of numbers:\n", salaries)

# for pay in salaries:
#     print(pay)

#  MEAN
print(np.mean(salaries))
print(np.median(salaries))

# plt.hist(salaries, 100)
# plt.show()

salaries = np.append(salaries, 10000000)
print(np.mean(salaries))
print(np.median(salaries))

# plt.hist(salaries, 100)
# plt.show()

hour_data = np.random.randint(low=0, high=24, size=100)
print(hour_data)

print(stats.mode(hour_data))

# Standard Deviation and Variance
print("Std Dev:", salaries.std())
print("Variance:", salaries.var())
print("99988 ^ Squared is:", 99988*99988)

# Probability Functions and Data Distributions
# Uniform Distribution
uni_val = np.random.uniform(-20, 20, 1000)
plt.hist(uni_val, 20)
plt.show()

#  Percentiles
print("90 Percentile:", np.percentile(salaries, 90))

# Moments
# I Moment == mean
# II Moment == variance
# Skew
print("Skew:", stats.skew(salaries))
# Kurtosis
print("Kurtosis", stats.kurtosis(salaries))



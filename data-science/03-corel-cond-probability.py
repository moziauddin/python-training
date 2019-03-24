import numpy as np
import matplotlib.pyplot as plt

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def co_var(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)

pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000)

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
print(co_var(pageSpeeds, purchaseAmount))
print('Covar using NP:\n', np.cov(pageSpeeds, purchaseAmount))


# Fabricating a relationship
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
print(co_var (pageSpeeds, purchaseAmount))

#  Easier way to compute co-efficient for corelation
print(np.corrcoef(pageSpeeds, purchaseAmount))

# P(B|A) = P(A,B) / P(A)
from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchase = 0
for _ in range(100000):
    ageDecade = random.choice([20,30,40,50,60,70])
    purchaseProbability = float(ageDecade) /100
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchase +=1
        purchases[ageDecade] += 1

print('Totals:', totals)
print('Purchases:', purchases)
print('totalPurchase:', totalPurchase)

PEF = float(purchases[70]) / float(totals[70])
print('Purchase Probability of 70', PEF)
PF = float(totals[70])/100000
print('Probability of being 70: ', PF)

PE = float(totalPurchase) / 100000
print('Probability of Buying something', PE)
print('Purchasing something in 70s', PE * PF)

# Conditional Probability
print('Cond Probability:', (float(purchases[70]) /100000) / PF)

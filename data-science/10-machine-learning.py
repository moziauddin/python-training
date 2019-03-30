'''

Machine Learning

 - Supervised Learning and Unsupervised Learning


'''

import numpy as np
import matplotlib.pyplot as plt

# Generate random data
randData = np.random.normal(3,1,100)
val = np.random.normal(20,0,100) / randData

plt.scatter(randData, val)
plt.show()

# Split data
# Shuffle non-random data using np.random.shuffle
data80 = randData[:80]
data20 = randData[80:]

val80 = val[:80]
val20 = val[80:]

plt.scatter(data80, val80)
plt.scatter(data20, val20)
plt.show()

x = np.array(data80)
y = np.array(val80)

p4 = np.poly1d(np.polyfit(x, y, 8))

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

tx = np.array(data20)
ty = np.array(val20)

tp4 = np.poly1d(np.polyfit(tx, ty, 10))

txp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(txp, tp4(txp), c='y')
plt.show()

from sklearn.metrics import r2_score
r2 = r2_score(y, p4(x))
tr2 = r2_score(ty, tp4(tx))
print(r2, tr2)
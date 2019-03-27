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
plt.show()

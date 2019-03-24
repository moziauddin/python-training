import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(0, 0.5, 10000)
plt.hist(values, 100)
plt.show()
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
plt.plot(x, norm.pdf(x))
plt.show()

#  Multiple plots on one graph

plt.plot(x,norm.pdf(x))
plt.plot(x, norm.pdf(x,1,.5))
plt.show()

#  Save plot to a file
plt.plot(x,norm.pdf(x))
plt.plot(x, norm.pdf(x,1,.5))
plt.savefig("sample-fig.png", format="png")

# Adjusting Axes
axes = plt.axes()
axes.set_xlim([-15,15])
axes.set_ylim([0,2])
axes.grid()
plt.plot(x,norm.pdf(x), 'g-')
plt.plot(x, norm.pdf(x,1,.5), 'b-.')
plt.show()


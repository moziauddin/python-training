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
plt.savefig("02-sample-fig.png", format="png")

# Adjusting Axes
axes = plt.axes()
axes.set_xlim([-15,15])
axes.set_ylim([0,2])
axes.grid()  # Adding grid lines
plt.plot(x,norm.pdf(x), 'g-')
plt.plot(x, norm.pdf(x,1,.5), 'b-.')
plt.show()

# Labeling Axes and adding a legent
axes = plt.axes()
axes.set_xlim([-10,10])
axes.set_ylim([0,2])
axes.grid()
plt.xlabel('x-axis-test')
plt.ylabel('y-axis-test')
plt.legend(['X-One', 'Y-One'], loc=3)
plt.plot(x,norm.pdf(x), 'y--')
plt.plot(x, norm.pdf(x,1,0.2), 'g:')
plt.show()

# XKCD Style
plt.xkcd()  # Enables XKCD mode
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate('Failure', xy=(70,1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(data)
plt.xlabel('time')
plt.ylabel('my success')
plt.show()

plt.rcdefaults()

# PIE Chart
val = [12, 55, 23, 84, 33, 5]
col = ['b', 'y', 'r', 'c', 'm', 'k']
explode = [0,0,0,0,0,0.1]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
plt.pie(val, colors=col, labels=labels, explode=explode)
plt.title('Pie Example Chart')
plt.show()

# Scatter plaot

x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y)
plt.title('Scatter Plot Example')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.show()

# Box and Whisker Plot
uniformSkewed = np.random.rand(100) * 100 - 50
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * 50 - 100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()
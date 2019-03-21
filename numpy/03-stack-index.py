import numpy as np


a = [6,7,8]
print(a, a[0:1], a[-2])

b = np.array([6,7,8])
print(b, b[:1], b[-2])

# MultiD array

c = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(c[1,2])
print(c[0:2,2])  # Prints rows 0,1 and column 2
print(c[-1])  # Prints last row
print(c[-1,1:3])

print(c[:,1])  # Prints middle column and all rows
print(c.flat)
for cell in c.flat:
    print(cell)  # prints items in the flat one at a time

print('Ravel:', c.ravel())  # Print an array as a 1d list

d = np.arange(6).reshape(2,3)
e = np.arange(6,12).reshape(2,3)
print(d, '\n', e)
f = np.vstack((d,e))  # Vertical Stacking
print(f)
g = np.hstack((d,e))  # Horizontal stacking
print(g)

split_array = np.hsplit(g,3)
for idx,ar in enumerate(split_array):
    print('Index:', idx)
    print('Array:\n', ar)

h = e < d
print(h)

print(d[d<e])  # Returns elements that satisfy the condition
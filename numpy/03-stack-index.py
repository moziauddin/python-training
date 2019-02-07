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

for cell in c.flat:
    print(cell)

print(c.ravel())
import numpy as np


a = np.array([1,2,3])
print('Dim size for A:', a.ndim)
print('Memsize for A:', a.itemsize)
print('Size of A:\n', a.size)
b = np.array([[1,1,1], [2,2,2], [3,3,3]])
print('Dim size for B:', b.ndim)
print('Mem size for B:', b.itemsize)
print('Type of B:', type(b[0]))
print('Size of B:\n', b.size)
print('Shape of B:\n', b.shape)

# Create array of zeroes
c = np.zeros((3,3))
print(c)

d = np.ones((3,3))
print(d)

e = np.arange(1,21)
print(e)

# Genrate 20 linearly spaced numbers between 2 and 8
f = np.linspace(2,8,20)
print(f)

# Initialize an array with custom data type
g = np.array([[1,1,1], [2,2,2], [3,3,3]], dtype=complex)
print(g)

h = np.array([[1,1,1], [2,2,2], [3,3,3]], dtype=int)
print(h.itemsize)

i = np.array([[1,2,3], [3,4,5]])
print(i.shape)
print(i.reshape(3,2))  # Change is temporary in shape
print(i)  # Not inplace

print(i.ravel())  # Change is temporary in shape
print('Min:', i.min(), 'Max:', i.max(), 'Sum all Cells:', i.sum(), 'Sum all Columns separately:', i.sum(axis=1))
print('SQRT of each cell:', np.sqrt(i), '\nStd Dev of the whole array:', np.std(i))

j = np.array([[1,2], [3,4]])
k = np.array([[5,6], [7,8]])
print('J is:\n', j, '\nK is:\n', k)
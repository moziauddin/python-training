import numpy as np
import time
import sys



# Low memory usage by Numpy Array Demo
print('Memopry Usage')
array = np.arange(1000)
print('Memory Used by a NumPy array of 1000 items', array.size*array.itemsize)

range1 = range(1000)
# print(range1)
print('Memory Used by a simple array of 1000 items', sys.getsizeof(5)*len(range1))  # Returns the size in memory of
# print(sys.getsizeof(5))
# print(len(range1))

# Speed of NumPy
print('Speed of NumPy')
size = 1000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
add1 = [(x+y) for x,y in zip(l1,l2)]
print("Adding Python Lists took", (time.time()-start)*1000, 'sec')

start = time.time()
add2 = a1 + a2  # Direct addition is possible as these are numpy lists, otherwise we need a list and for loop
print('Adding NumPy lists took', (time.time()-start)*1000, 'sec')
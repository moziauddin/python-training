import numpy as np


a = np.arange(12).reshape(3,4)
print(a)

for row in a:
    for cell in row:
        print(cell)

for i in a.flatten():# One line to print cells
    print('cell:', i)

print(a.flatten())

for i in np.nditer(a, order='F'):  # Fortran iteration, column by column
    print(i)

for i in np.nditer(a, order='F', flags=['external_loop']):  # Fortran iteration, column by column, each column in one line
    print(i)

for i in np.nditer(a,order='F', op_flags=['readwrite']):  # Changes the existing array
    i[...]=i*i  #Each cell is its square, inplace update
print(a)

b = np.arange(6).reshape(3,2)
c = np.arange(3).reshape(3,1)
# Iterate through two arrays by row in each array
for x,y in np.nditer((b,c)):
    print(x,y)

print(np.arange(1,10,2))
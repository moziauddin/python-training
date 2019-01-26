a = 233
b = 400
c = 32
d = 2

# Addition
print(a + b)

# Subtraction
print(a - b)

# Simple Division
print(c/d)
print(d / c)

# Whole number / Integer division
print(c // d)
print(d // c)

# Multiplication
print(b * d)
print(b ** d)

# Remainder
print(a % c)

# BEDMAS
print(20-10/5*3**2)
print(d + (d - c / a) * d + b)

# Print all declared variable names...
print(dir())

# Type checking
print(type(2))
print(type(2.0))
print(type('2'))
print(type(2.5464617854164651416))
print(type(24687167186546514684168168716868161461846146848455555555555555555555555555555555555555555555555555))

'''
OUTPUT:
---------------------------
633
-167
16.0
0.0625
16
0
800
160000
9
2.0
405.725321888412
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'd']
<class 'int'>
<class 'float'>
<class 'str'>
<class 'float'>
<class 'int'>
'''
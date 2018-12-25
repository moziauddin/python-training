# String examples

a = 'python'
b = 'learning'
c = 22
print(a + ' ' + b)
# Adding different types will lead to error
# Ex: print(a + ' ' + c)

# Print a string to different cases using functions of class String
print(a.upper(), b.title())

# Lower case print
print("Lowercase:", a.lower())

# String Length
print(len(a))

# Print certain charanter in a string by index in uppercase
print(a[2].upper())
print(a[-3].upper())

# Print characters of a string from and to a position
print(a[:4])  # Begining to 4 charanters, index 4 is not inclusive
print(a[2:6])  # From 3rd char to 5th, 6 is not inclusive

# Print a string multiple times repeatedly
print(a * 10)
print((a + ' ') * 10)  # With spaces

# Print a triangle pattern
for i in range(5):
    print('*' * i)

'''
Output:
----------------------------------------------
python learning
PYTHON Learning
Lowercase: python
6
T
pyth
thon
pythonpythonpythonpythonpythonpythonpythonpythonpythonpython
python python python python python python python python python python 

*
**
***
****
'''
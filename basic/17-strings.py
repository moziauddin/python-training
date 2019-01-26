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

char = 'can you do it?'

# Methods available for a string/integer
print(char.replace('o', 'i'))
print(dir(char))
print(help(char.replace))
print(char.replace('o', 'i', 1))


'''
Output:
----------------------------------------------
python learning
PYTHON Learning
Lowercase: python
6
T
H
pyth
thon
pythonpythonpythonpythonpythonpythonpythonpythonpythonpython
python python python python python python python python python python 

*
**
***
****
can yiu di it?
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
Help on built-in function replace:

replace(...) method of builtins.str instance
    S.replace(old, new[, count]) -> str
    
    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

None
can yiu do it? 
'''
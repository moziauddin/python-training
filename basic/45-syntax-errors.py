'''
We have syntax errors and exceptions in Python
----------------------------------------------
SyntaxError: invalid syntax - int is a function and needs paranthesis in the below case
    int 9
        ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(3)? - Print is wronly formatted

    a = [1, 2, 3}
                ^
SyntaxError: invalid syntax

'''
# Syntax Errors
print(2)
int(10)
int(9)
print(3
      )
print(2)

a = [1, 2, 3]

# ----------------------
# ----------------------
'''
    print(a + b)
        ^
SyntaxError: invalid syntax - Previous line has incomplete brackets for print statement

TypeError: unsupported operand type(s) for +: 'int' and 'str'

    print(522/0)
ZeroDivisionError: division by zero
'''
# Exceptions

a = 1
b = '2'
print(int(2.5))
print(a + int(b))
print(522/8)

def divide(a, b):
    try:
        return a/b
    except:
        print("You cannot divide by 0")

divide(34, 0)
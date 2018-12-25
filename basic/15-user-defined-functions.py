# Example Functions with out any arguments and return types
def myfirstfunction():
    print("Python User Defined Function")

myfirstfunction()

def getname():
    name = input('Enter your name: ')
    print("Your name is :", name)

getname()

def addfunction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = num1 - num2
    num4 = num1 + num2
    print("Addition:", num4, "Subtraction: ", num3)

addfunction()
print('----------------------------------------------')
# Example Functions with arguments

def addfunctionwithargs(n1, n2):
    n4 = n1 + n2
    print(n1, "+", n2, "=", n4)
    n3 = n1 - n2
    print(n1, "-", n2, "=", n3)
addfunctionwithargs(4,5)
print('----------------------------------------------')
'''
Output: 
-----------------------------
Python User Defined Function
Enter your name: mo
Your name is : mo
Enter the first number: 11
Enter the second number: 2
Addition: 13 Subtraction:  9
'''
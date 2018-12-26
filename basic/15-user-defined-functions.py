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


def age_in_secs():
    age_years = int(input("Enter your age in years: "))
    age_secs = age_years * 365 * 24 * 60 * 60
    print("Your age is {} in seconds...".format(age_secs))


age_in_secs()
'''
Output: 
-----------------------------
Python User Defined Function
Enter your name: Mo
Your name is : Mo
Enter the first number: 12
Enter the second number: 11
Addition: 23 Subtraction:  1
----------------------------------------------
4 + 5 = 9
4 - 5 = -1
----------------------------------------------
Enter your age in years: 35
Your age is 1103760000 in seconds...
'''
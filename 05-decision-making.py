# IF Statement
a = 10
if a == 10:
    print(a)
    print("A is now 10")

if a == 11:
    print("A is now 11")

# Nested IF
x = 1
y = 2
z = 3
if x == 1:
    print(x)
    if y == 2:
        print(y)
    if z == 3:
        print(z)
print('-------------------')
# Else If
if x == 12:
    print(x)
elif y == 2:
    print(y)
else:
    print(z)
print('-------------------')

# Number even or not by accepting input

num = input("Enter any number: ")
if int(num) % 2 == 0:
    print("Number you entered is : EVEN")
else:
    print("You entered an ODD number")
input("Press any key to exit...")
print('-------------------')

# Check if a  character is a vowel
# If you miss the paranthesis for each condition, it returns a type operator error
char = input("Enter any alphabet: ")
if (char == 'a') | (char == 'e') | (char == 'i') | (char == 'o') | (char == 'u'):
    print(char, "is a VOWEL")
else:
    print(char, "is a consonant")

print('-------------------')

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter last number"))
if (num1 > num2) & (num1 > num3):
    print(num1, "is the greatest of all three")
elif (num2> num1) & (num2 > num3):
    print(num2, "is the greatest of all three numbers")
else:
    print(num3, "is the greatest of all three numbers")

'''
OUTPUT:
-------------------------------------------
10
A is now 10
1
2
3
-------------------
2
-------------------
Enter any number: 3
You entered an ODD number
Press any key to exit...
-------------------
Enter any alphabet: i
i is a VOWEL
-------------------
Enter first number111
Enter second number222
Enter last number1
222 is the greatest of all three numbers

'''
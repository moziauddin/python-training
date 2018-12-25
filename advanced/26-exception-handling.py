num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    num3 = num1 / num2
except:
    print("You cannot divide a number by \'0\'")
else:
    print("Division:", num1/num2)

'''
Output:
-------------------------
Enter the first number: 0
Enter the second number: 0
You cannot divide a number by '0'
'''
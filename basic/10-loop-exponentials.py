# Exponentials
num = int(input("Please enter a number: "))
exp = int(input("Please enter an exponent: "))
total = 1
for i in range(1,exp+1):
    total = total * num
print("The result is: ", total)

'''
Output:
---------------
Please enter a number: 2
Please enter an exponent: 3
The result is:  8
'''
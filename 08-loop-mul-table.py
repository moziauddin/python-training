# MULTIPLICATION TABLE - Using For
num = int(input("Please enter a Number: "))
for i in range(11):
    print(num, "x", i, "=", (num*i))

print('------------------------------------')

i = 1
while i <= 10:
    print(num, "x", i, "=", (num * i))
    i = i + 1

'''
Output:
------------------------------------
Please enter a Number: 4
4 x 0 = 0
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
------------------------------------
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
'''
# FOR Loop - Basic
for i in range(6):
    print(i)

print('------------------------')
# FOR Loop - change start number
for i in range(1, 6):
    print(i)

print('------------------------')
# FOR Loop - Change increment number
for i in range(0, 20, 5):
    print(i)

print('------------------------')
# FOR Loop - Using another number
num = 0
for i in range(5):
    num = num + i
    print(num)
print('------------------------')
# WHILE Loop - Manually manage the increment variable
i = 0
while(i < 5):
    print(i)
    i = i + 1
# If you forget to increment the variable i, it wil cause infinite loop

print('------------------------')

'''
Output:
----------------------------------
0
1
2
3
4
5
------------------------
1
2
3
4
5
------------------------
0
5
10
15
------------------------
0
1
3
6
10
------------------------
0
1
2
3
4
------------------------
'''
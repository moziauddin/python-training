# Same as previous example
# Delay printing of table to user input

num = int(input("Build tables upto? Pick a number:"))
for i in range(1, num):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print('-------------')
    input("Press Enter key to print next table")

'''
Output:
Build tables upto? Pick a number:2
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
-------------
Press any key to print next table
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
-------------
Press any key to print next table

'''
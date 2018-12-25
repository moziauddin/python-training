# Continue statement demo

i = 1
while i < 10:
    i = i + 1
    if i < 5:
        continue
    print(i)

'''
Output:
-----------
5
6
7
8
9
10
'''
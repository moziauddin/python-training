# Continue statement demo

i = 1
while i < 10:
    i = i + 1
    if i < 8:
        continue
    print(i*10)

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
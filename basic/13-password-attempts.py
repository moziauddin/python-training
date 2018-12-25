password = "python"
for i in range(3):
    pwd = input('Please enter your password: ')
    if pwd == password:
        print("Congratulations, you are logged in")
        break
    else:
        print("Wrong password! You have", 2-i, "changes left..")
        continue

'''
Output:
--------------------------------------------
Please enter your password: as
Wrong password! You have 2 changes left..
Please enter your password: ds
Wrong password! You have 1 changes left..
Please enter your password: ed
Wrong password! You have 0 changes left..
--------------------------------------------
Please enter your password: python
Congratulations, you are logged in
'''
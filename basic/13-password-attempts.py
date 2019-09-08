one_to_nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
password = input('Enter a secure password, atleast 8 character long and : ')
len_val = 1
nums_len = 1

nums = 0

while nums_len:
    # Password Length Check
    while len_val:
        if len(password) < 9:
            password = input('Password too short, Enter a new password: ')
        else:
            break

    # Password numbers check
    for i in password:
        for n in one_to_nine:
            try:
                if int(i) == n:
                    nums += 1
            except:
                continue
    print('Nums:', nums)
    try:
        if nums <= 0:
            password = input('Password needs to have at least one number, Enter a new password: ')
        else:
            nums_len = 0
    except:
        continue

    # Look for three attempts
    for i in range(3):
        if password == 'Password123':
            print("Congratulations, you are logged in")
            break
        elif i == 2:
            print('Game Over')
        else:
            print(2 - i, "chances left")
            password = input("Wrong password! Enter a new Password:")
            continue
'''
Output:
--------------------------------------------

'''
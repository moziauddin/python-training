# Guess a magic number
import random


magic_num = random.randint(1,10)
user_guess = int(input("Please enter a number between 1 and 10: \n"))
if user_guess == magic_num:
    print("Congratulations, you win")
else:
    print("You were unsuccessful, please try again...")

'''
Output:
--------------------------------
Please enter a number between 1 and 10: 
3
You were unsuccessful, please try again...

Please enter a number between 1 and 10: 
10
Congratulations, you win
'''

# Formatting print statements using %s, %.2f, etc
# %d - integer
# %f - floating point
# %s - string value

name = 'Neo'
age = 33
occupation = 'Hacker'
temp = 89.9
rating = 4.90

# C like formatting
print("%s is a %s. He is %d years old. Its is %.1f outside at the moment. He is rated ar %.2f"
      % (name, occupation, age, temp, rating))

# List based formatting
print("{} is a {}. He is {} years old. Its is {} outside at the moment. He is rated ar {}"
      .format(name, occupation, age, temp, rating))

# List based formatting with changed positions
# List based formatting
print("{1} is a {0}.".format(name, occupation))
print("{:4} is a {:8}.".format(name, occupation))  # Adds spaces for padding

# Format using a tuple and .format function with padding
for i in range(1, 11):
    print("{:2} {:3} {:3}".format(i, i*i, i*i*i))

'''
Output:
--------------------------------
Neo is a Hacker. He is 33 years old. Its is 89.9 outside at the moment. He is rated ar 4.90
Neo is a Hacker. He is 33 years old. Its is 89.9 outside at the moment. He is rated ar 4.9
Hacker is a Neo.
Neo  is a Hacker  .
 1   1   1
 2   4   8
 3   9  27
 4  16  64
 5  25 125
 6  36 216
 7  49 343
 8  64 512
 9  81 729
10 100 1000

'''
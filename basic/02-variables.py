a = 21
b = "Mo"
c = 21.98
d = "11" # This is a string
# Adding unlike types results in error
# print (c + d) WILL FAIL
print(c + int(d))

# Print Multiple Values in one line
emp_name = "Mo"
emp_sal = "Mr. "
emp_num = 10112
emp_salary = 1000

# Just print variables in one line
print(emp_salary, emp_num, emp_name)

# Form a sentence using str function to convert variables to strings you can concatenate
print(emp_name + " bears employee number " + str(emp_num) + " and earns $" + str(emp_salary))

# Repeat the above without + :: Also this method adds the extra spaces
print(emp_sal, emp_name, "bears employee number", emp_num, "and earns $", emp_salary)

# Adding two strings
print(emp_sal, emp_name)

'''
OUTPUT: 
-----------------------------------------------------
32.980000000000004
1000 10112 Mo
Mo bears employee number 10112 and earns $1000
Mr.  Mo bears employee number 10112 and earns $ 1000
Mr.  Mo
'''



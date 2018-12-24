# FACTORIAL - Using For
fact = 1
num = int(input("Please enter a number: "))
for i in range(1, (num + 1)):
     fact = fact * i
print("Factorial of", num, "is", fact)

print('-------------------------------------------')

# FACTORIAL - Using While
i = 1
fact = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("Factorial of", num, "is", fact)

print('-------------------------------------------')
'''
Output:

Please enter a number: 99
Factorial of 99 is 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000
-------------------------------------------
Factorial of 99 is 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000

'''
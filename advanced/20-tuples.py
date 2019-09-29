tup1 = 1, 2, 3, 4, 5
tup2 = ('Neo', 23, "Hacker")

print('Tuple1:', tup1)
print('Tuple2:', tup2)

# Tuples are permanent lists and cannot be changed
# Return index of a element by value
print(tup1.index(4))
# Returns how many instances of an element exist in a tuple
print(tup2.count('Neo'))

'''
Output:
-------------------------
Tuple1: (1, 2, 3, 4, 5)
Tuple2: ('Neo', 23, 'Hacker')
3
1
'''
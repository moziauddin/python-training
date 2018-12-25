# List Methods
list1 = ['peter', 44, 'Rachel', 9, 99]
# Print list items one in each row
for i in list1:
    print(i)

list1.append('Rachel')
print("Appended Rachel to the end of the list:", list1)
# Print how many times a element exists in a list
print("Number of times Rachel occurs in list1 is", list1.count('Rachel'))
print("Index of first instance of Rachel is", list1.index('Rachel'))
# Remove first instance of a element based on its value
list1.remove('Rachel')
print("Removed first instance of rachel", list1)

# Reverse a list
list1.reverse()
print("Reversed List", list1)

# Print sorted List
#print(list1.sort())  # Only works when type is same for all elements

# Remove an item from the list
print(list1.pop())
print("After deleting the last item", list1)

'''
Output:
-----------------------------
peter
44
Rachel
9
99
Appended Rachel to the end of the list: ['peter', 44, 'Rachel', 9, 99, 'Rachel']
Number of times Rachel occurs in list1 is 2
Index of first instance of Rachel is 2
Removed first instance of rachel ['peter', 44, 9, 99, 'Rachel']
Reversed List ['Rachel', 99, 9, 44, 'peter']
peter
After deleting the last item ['Rachel', 99, 9, 44]

'''
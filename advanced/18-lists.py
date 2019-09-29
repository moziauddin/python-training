# List examples
list1 = [45]
print(list1)
list1 = [22, 32, 44, 22, 12, 76, 56, 99, 0]
print("Items in the list are: ", list1)
print("5th Item in the List is:", list1[4])
print("-2th Item in the List is:", list1[-2])
# Print list length
print("Length: ", len(list1))
# Change an element in a list
print("Before: ", list1)
list1[0] = 33
print("After:", list1)

# # Print n items from a list from different starting point
print(list1[:3])  # Print first 3 items
print(list1[1:])  # Print items 2 to end
print(list1[2:4])  # Print 3 and 4; last index is exclusive
#
# # List of Strings
list2 = ['pheobe', 'rachel', 'monica', 'emily', 'janet', 'mona']
print(list2[:3])  # Print first 3 items
print(list2[1:])  # Print items 2 to end
print(list2[2:4])  # Print 3 and 4; last index is exclusive
print("Length: ", len(list2))
print("Length: ", len(list2[3]))
print(list2[-2])
#
# # Compare Lists
list3 = ['pheobe', 'rachel', 'monica', 'emily', 'amanda', 'linda']
print(list2 == list3)
print("Addition:", list2 + list3)
#
# # Versatile data-type
list4 = [2, 66, 'Ronny', 'Mo', ["Mel", 788, 10.5]]
print("List4: ", list4)

'''

Output:
----------------------------------------
45
Items in the list are:  [22, 32, 44, 22, 12, 76, 56, 99, 0]
5th Item in the List is: 12
-2th Item in the List is: 99
Length:  9
Before:  [22, 32, 44, 22, 12, 76, 56, 99, 0]
After: [33, 32, 44, 22, 12, 76, 56, 99, 0]
[33, 32, 44]
[32, 44, 22, 12, 76, 56, 99, 0]
[44, 22]
['pheobe', 'rachel', 'monica']
['rachel', 'monica', 'emily', 'janet', 'mona']
['monica', 'emily']
Length:  6
Length:  5
janet
False
Addition: ['pheobe', 'rachel', 'monica', 'emily', 'janet', 'mona', 'pheobe', 'rachel', 'monica', 'emily', 'amanda', 'linda']
[2, 66, 'Ronny', 'Mo']

'''
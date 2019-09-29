# Dictionaries are lists of key-value pairs
dict1 = {}
print("Empty Dictionary", dict1)
dict1 = {'name': 'Neo', 'age': 23, 'job': 'Hacker', 'cars': ['chevy', 'ford']}
print("Dictionary with items:", dict1)
print("After Clearing:", dict1.clear())
dict1 = {'name': 'Neo', 'age': 23, 'job': 'Hacker'}

# Get values using the keys
print(dict1["name"], "is", dict1["age"], "years old. He is a", dict1["job"], ".")
# Add key value pair to the dictionary
dict1["hobby"] = 'Phishing'
print(dict1["name"], "is", dict1["age"], "years old. He is a", dict1["job"], ". His hobby is", dict1["hobby"], ".")
print(dict1)

# Delete a key value pair
del dict1["age"]
print(dict1)

dict33 = dict(abc=123)
print(dict33)

'''
Output:
-----------------------------
Empty Dictionary {}
Dictionary with items: {'name': 'Neo', 'age': 23, 'job': 'Hacker'}
After Clearing: None
Neo is 23 years old. He is a Hacker .
Neo is 23 years old. He is a Hacker . His hobby is Phishing .
{'name': 'Neo', 'age': 23, 'job': 'Hacker', 'hobby': 'Phishing'}
{'name': 'Neo', 'job': 'Hacker', 'hobby': 'Phishing'}
'''
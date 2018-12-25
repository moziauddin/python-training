# Create a sample class
# Create an object for the class


class Person:
    def __init__(self):
        self.balance = 0
        self.pos = []
        print("Ran __init__ function")

    def details(self, name, age):
        self.name = name
        self.age = age
        print("{} is {} years old...".format(name, age))

    def buystuff(self, item):
        self.pos.append(item)
        print("Bought and stored:", item)

    def borrow(self, amt):
        self.balance += amt
        print("Added {} to balance".format(amt))

p1 = Person()
p1.details("Mo", "34")
print("Name is:", p1.name)
print("Age is:", p1.age)
p1.buystuff('Car')
print("P1's current pocessions are:", p1.pos)
p1.borrow(200)
print("The current balance is", p1.balance)

'''
Output:

-----------------------------------------
Ran __init__ function
Mo is 34 years old...
Name is: Mo
Age is: 34
Bought and stored: Car
P1's current pocessions are: ['Car']
Added 200 to balance
The current balance is 200
'''
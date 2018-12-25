# Python special functions


class Person:
    def __init__(self, name, age):
        print("Hello there, {}".format(name))
        self.name = name
        self.age = age

    def __str__(self):
        # Without str function, printing the object will return memory location
        return "name: {}\nage: {}".format(self.name, self.age)

    def __del__(self):
        # To delete the object, called when instance is deleted
        print("{} just expired, memory is free".format(self.name))


p1 = Person('Mo', 33)
print(p1)
del p1

'''
Output:

Hello there, Mo
name: Mo
age: 33
Mo just expired, memory is free
'''
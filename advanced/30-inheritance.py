class Person:
    def __init__(self, name, age):
        print("Hello there, {}".format(name))
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: {}\nAge:{}".format(self.name, self.age)


class Teacher(Person):
    def __init__(self, name, age, sub):
        Person.__init__(self, name, age)
        self.sub = sub

    def __str__(self):
        return Person.__str__(self)+"\nSub: {}".format(self.sub)


t1 = Teacher("Roger", 54, 'Economics')
print(t1.name, t1.age, t1.sub)
print(t1)

'''
Output:
----------------------
Hello there, Roger
Roger 54 Economics
Name: Roger
Age:54
Sub: Economics
'''
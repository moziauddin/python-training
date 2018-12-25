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
        return Person.__str__(self) + "\nSub: {}".format(self.sub)


t1 = Teacher('Martin', 47, 'Organic Chemistry')
print(t1)

'''
Output:
--------------------------
Hello there, Martin
Name: Martin
Age:47
Sub: Organic Chemistry

'''
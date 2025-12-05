#-------------inheritance--------------

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old")

class Employee(Person):
    pass

emp1 = Employee("edu", 25)

emp1.display_info()
emp1.age = 37
emp1.display_info()


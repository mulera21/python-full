#-------------inheritance--------------

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old")

class Employee(Person):
    pass

emp1 = Employee()


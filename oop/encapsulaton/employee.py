#---------------encapsulation-----------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"name is: {self.name} and the salary is: {self.salary}")
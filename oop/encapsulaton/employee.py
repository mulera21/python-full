#---------------encapsulation-----------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # private attribute

    def get_salary(self):

        """public getting salary"""
        return self.__salary
    
    def display(self):
        """public getting name and salary"""
        print(f"name is: {self.name} and the salary is: {self.salary}")

employee = Employee('mike', 1500)
employee.display()
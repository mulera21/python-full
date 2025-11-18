#---------------encapsulation-----------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # private attribute

    def get_salary(self):

        """public getting salary"""
        return self.__salary
    
    def set_salary(self, new_salary):
        """Public method to set salary with validation (setter)"""
        if new_salary >= 0:  # validation
            self.__salary = new_salary
            print(f"Salary updated to: ${new_salary}")
        else:
            print("Error: Salary cannot be negative!")
    
    def display(self):
        """public getting name and salary"""
        print(f"name is: {self.name} and the salary is: {self.get_salary()}")

#using the class
employee = Employee('mike', 1500)
employee.display()

# Get salary using getter
print(f"Current salary: ${employee.get_salary()}")  # Current salary: $1500
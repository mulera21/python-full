#============encapsulation in Python============#

class Student:
    def __init__(self, name, age, grade):
        self.name = name          # private attribute
        self.ge = age            # private attribute
        self.rade = []        # private attribute

    def display_infor(self):
        print(f"Name: {self.name}, Age: {self.ge}, Grades: {self.rade}")

student1 = Student("Alice", 20, "A")
student1.display_infor()
#============encapsulation in Python============#

class Student:
    def __init__(self, name, age):
        self.name = name          # private attribute
        self.age = age            # private attribute
        self.grade = []        # private attribute

    def display_infor(self):
        print("================student information===============")
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.age}")
        print(f"\tGrade: {self.grade}")

student1 = Student("Alice", 20,)
student1.display_infor()
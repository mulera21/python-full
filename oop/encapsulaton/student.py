#============encapsulation in Python============#

class Student:
    def __init__(self, name, age):
        self.name = name       
        self.age = age            
        self.__grade = []        # private attribute

    def display_infor(self):
        print("================student information===============")
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.age}")
        print(f"\tGrade: {self.__grade}")
    def add_grade(self, grade):
        if 0<grade<=100:
            self.__grade.append(grade)
            print(f"Grade{grade} added for {self.__grade}")
        else:
            print("invalid grade it shhould be 0 to 100")





student1 = Student("Alice", 20,)
student1.display_infor()
student1.grade.append(100)
student1.display_infor()
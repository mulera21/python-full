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
        print(f"\tAverage: {self.get_average()}")

    def add_grade(self, grade):
        if 0<grade<=100:
            self.__grade.append(grade)
            print(f"Grade {grade} added for {self.name}")
        else:
            print("invalid grade it shhould be 0 to 100")
    
    def get_average(self):
        if len(self.__grade)>0:
            average = sum(self.__grade) / len(self.__grade)
            return average
        else:
            return 0





student1 = Student("Alice", 20,)
student1.display_infor()
student1.add_grade(34)
student1.add_grade(50)
student1.add_grade(76)
student1.display_infor()


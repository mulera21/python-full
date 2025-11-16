#----------------student management system-----------------#

class Student:
    def __init__(self, name , student_id, major):
        self.name =name
        self.student_id = student_id
        self.major = major
    
    def get_details(self):
        return {
            "Name": self.name,
            "Student ID": self.student_id,
            "Major": self.major
        }
    
student1 = Student("Alice Johnson", "S12345", "Computer Science")
student1_details = student1.get_details()
print(student1_details)
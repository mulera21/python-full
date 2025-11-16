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
    def enroll(self, course):
        return f"Student {self.name} has enrolled in {course}."   

print("------------Student Management System------------")
student1 = Student("Alice Johnson", "S12345", "Computer Science")
student1_details = student1.get_details()

print("-----student1_details enrolled --------")
enrollment_message = student1.enroll("Math 101")
print(student1_details)
print(enrollment_message)
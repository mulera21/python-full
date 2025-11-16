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
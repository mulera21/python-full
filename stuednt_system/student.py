#----------------student management system-----------------#

class Student:
    def __init__(self, name , student_id, major):
        self.name =name
        self.student_id = student_id
        self.major = major
        self.enrolled_courses = [] #list
    
    def get_details(self):
        return {
            "Name": self.name,
            "Student ID": self.student_id,
            "Major": self.major,
            "Enrolled Courses": self.enrolled_courses
        }
    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            return f"Student {self.name} has enrolled in {course}." 
        else:
            return f"Student {self.name} is already enrolled in {course}."  

    def drop_course(self, course):
        return f"Student {self.name} has dropped the course {course}." 
    def pay_tuition(self, amount):
        return f"Student {self.name} has paid tuition of ${amount}."

print("------------Student Management System------------")
student1 = Student("Alice Johnson", "S12345", "Computer Science")
student1_details = student1.get_details()
print(student1_details)

print("-----student1_details enrolled --------")
enrollment_message = student1.enroll("Math 101, Physics 201, Chemistry 301, Literature 101, History 201")
print(enrollment_message)

print("-----student1_details dropped course --------")
drop_message = student1.drop_course("Math 101")
print(drop_message)

print("-----student1_details paid tuition --------")
tuition_message = student1.pay_tuition(5000)
print(tuition_message)

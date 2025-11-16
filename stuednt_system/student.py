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
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            return f"Student {self.name} has dropped the course {course}." 
        else:
            return f"Student {self.name} is not enrolled in {course}." 
    def pay_tuition(self, amount):
        return f"Student {self.name} has paid tuition of ${amount}."
    def show_enrolled_courses(self):
        return f"Student {self.name} is enrolled in the following courses: {', '.join(self.enrolled_courses)}"  
    
def main():
    print("------------Student Management System------------")
     #get information from user
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    major = input("Enter student major: ")

    student1 = Student(name, student_id, major) #create object

    while True:
        print("\n student Menu:")
        print("1. View Student Details")
        print("2. Enroll in a Course")
        print("3. Drop a Course")
        print("4. Pay Tuition")
        print("5. Show Enrolled Courses")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            details = student1.get_details()
            for key, value in details.items():
                print(f"{key}: {value}")
        elif choice == '2':
            course = input("Enter course name to enroll: ")
            message = student1.enroll(course)
            print(message)
        elif choice == '3':
            course = input("Enter course name to drop: ")
            message = student1.drop_course(course)
            print(message)
        elif choice == '4':
            amount = float(input("Enter tuition amount to pay: "))
            message = student1.pay_tuition(amount)
            print(message)
        elif choice == '5':
            courses_message = student1.show_enrolled_courses()
            print(courses_message)
        elif choice == '6':
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

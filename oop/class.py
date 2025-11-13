#-----oop-------------------
#classes oop

class Student:
    def __init__(self, name):
        self.name = name
    name = "John Doe" #class attribute

student1 = Student() #create an object of the class
student2 = Student() #create another object of the class

print(student1.name) #accessing class attribute
print(student2.name) #accessing class attribute

#--------------------------------method in class--------------------------------#
class Person:
    
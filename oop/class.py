#-----oop-------------------
#classes oop

class Student:
    def __init__(self, name):
        self.name = name
    name = "John Doe" #class attribute

student1 = Student("Alice") #create an object of the class
student2 = Student("Bob") #create another object of the class

print(student1.name) #accessing class attribute
print(student2.name) #accessing class attribute

#--------------------------------method in class--------------------------------#
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

mycar = Car("Toyota", 2020) #create an object of the class
print(f"my car model is {mycar.model} and is model year {mycar.year}") #accessing instance attribute
 #accessing instance attribute
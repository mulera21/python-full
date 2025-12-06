#------------------polymorphism/overriding.py------------------

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks") 

class Cat(Animal):
    def speak(self):
        print("The cat meows")
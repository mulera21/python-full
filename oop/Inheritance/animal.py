#---------------------animal inheritance---------------

class Animal:
    def __init__(self, name):
        self.name =name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class mammal(Animal):
    pass

class Bird(Animal):
    pass

class Reptile(Animal):
    pass

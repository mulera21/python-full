#---------------------animal inheritance---------------

class Animal:
    def __init__(self, name):
        self.name =name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Reptile(Animal):
    pass

cat = Mammal("cute")
cat.eat()

parrot = Bird("pinky")
parrot.sleep()

snake = Reptile("spokey")
snake.eat()
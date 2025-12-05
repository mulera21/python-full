#---------------------animal inheritance---------------

class Animal:
    def __init__(self, name):
        self.name =name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Mammal(Animal):
    def nurse(self):
        print(f"{self.name} is nursing")
class Dog(Mammal):
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is swimming on water")

class Reptile(Animal):
    def kill(self):
        print(f"{self.name} is hiding")

cat = Mammal("cute")
cat.eat()
cat.nurse()

parrot = Bird("pinky")
parrot.sleep()
parrot.fly()

snake = Reptile("spokey")
snake.eat()
snake.kill()

# class dog
mydog = Dog("mike")
mydog.sleep()
mydog.fetch()
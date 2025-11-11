#--------------------------------function.py--------------------------------#
def hello():
    print("Hello, World!")

hello()
#--------------------------------function.py--------------------------------#

#--------------------------------function parameter--------------------------------#
def show_message(msg):
    print("This is a sample function.", msg)

show_message("Function executed successfully.")

#--------------------------------function two parameter--------------------------------#

def sum(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} + {num2} is: {result}")

sum("hell0", "nice")

#--------------------------------function two parameter specify the type--------------------------------#
def multiply(num1: int, num2: int):
    result = num1 * num2
    print(f"The multiplication of {num1} * {num2} is: {result}")
    return result

multiply(5, 4)

#--------------------------------function key value argument--------------------------------#

def display_info(name = None, age=None):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Alice")

#--------------------------------Arbitrary Arguments--------------------------------#

def showValues(*args):
    for value in args:
        print(f"Value: {value}")
showValues(10, 20, 30, "nice", 50)

#--------------------------------Arbitrary Keyword Arguments--------------------------------#

def showDetails(**kwargs):  #arbitrary keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
showDetails(name="Bob", age=30, city="New York")

#--------------------------------Arbitrary Value Arguments--------------------------------#

def displayInfo(**kwargs): 
    for value in kwargs.values():
        print(f"Value: {value}")  
displayInfo(name="Charlie", age=28, country="USA")

#--------------------------------args and kwargs--------------------------------#
def showData(*args, **kwargs):
    print("-----------args-----------")
    for item in args:
        print(f"Arg: {item}")
    print("-----------kwargs-----------")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

showData(1, 2, 3, name="David", age=35)
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
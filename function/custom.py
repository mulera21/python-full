# function/custom.py

def say_hello():
    print("Hello,BMW !")
say_hello()

# 运行结果
#function with arguments/parameters
#default parameter value
#guest


def greet_user(name = "Guest"):
    print(f"Hello, {name}!")
greet_user()


# 运行结果
# Hello, Guest!
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Alice")




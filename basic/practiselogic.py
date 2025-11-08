#logic
print("Welcome to the color mixer")
print("Available colors: red, blue, yellow")
print("Mix two primary colors to get a secondary color")
print("------------------------------------------")
user_1 = input("ENTER First Color  ")
user_2 = input("ENTER Second Color  ")

if user_1 == 'red' and user_2 == 'blue' or user_1 == 'blue' and user_2 == 'red':
    print("You have created purple🟣💜")
elif user_1 == 'red' and user_2 == 'yellow' or user_1 == 'yellow' and user_2 == 'red':
    print("You have created orange🧡")
elif user_1 == 'blue' and user_2 == 'yellow' or user_1 == 'yellow' and user_2 == 'blue':
    print("You have created green💚")
else:
    print("Invalid color combination🚨")
#end of code
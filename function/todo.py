#-----------to dolist-----------


def show_task(task):
    if task:
        print("Your Tasks:")
        for idx in task():
            print(f"\t- {idx}")
    else:
        print("No tasks available.")    
def add_task(task):
    pass
def remove_task(task):
    pass
task = []


while True:
    print("To Do List Application")
    print("---------To--Do--List----------")
    print("1. show Task")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    option = int(input("Enter your choice (1-4): "))

    if option == 1:
        show_task(task)
    elif option == 2:
         add_task(task)
    elif option == 3:
        remove_task(task)
    elif option == 4:
        break
    else:
        print("Invalid option. Please choose a number between 1 and 4.")    
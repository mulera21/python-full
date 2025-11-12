#-----------to dolist-----------


def show_task(task):
    if task:
        print("Your Tasks:")
        for idx, item in enumerate(task, 1):  # ✅ CORRECT: Iterate through the list
            print(f" \t -{idx}. {item}")
    else:
        print("No tasks available.")    
def add_task(task: list):
    input_task = input("Enter the task to add: ")
    task.append(input_task.lower)

def remove_task(task: list):
    input_task = input("Enter the task to remove: ").lower()
    if input_task in task:
        task.remove(input_task.lower())
        print(f"Task '{input_task}' removed.")
    else:
        print(f"Task '{input_task}' not found in the list.")
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
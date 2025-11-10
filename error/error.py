#error handling

try:

    print(1/0)
    print("This will not be printed.")
except:
    print("An error occurred: Division by zero.")
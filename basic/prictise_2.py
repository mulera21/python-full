#logic
#number guessing game
print("Welcome to the number guessing game")
print("Guess a number between 0 and 20")
print("------------------------------------------")

secrete_number = 15
user_1 = int(input("ENTER a number  "))
#logic to check the number
if user_1 == secrete_number:
    print("correct guess✅")
elif user_1 > 20:
    print("too high repeat again✅")
else:
    print("too low repeat again🚨")
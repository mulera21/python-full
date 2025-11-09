#logic
#number guessing game
print("Welcome to the number guessing game")
print("Guess a number between 0 and 20")
print("------------------------------------------")

user_1 = input("ENTER a number  ")
#logic to check the number
if int(user_1) >= 20:
    print("too high repeat again😒")
elif int(user_1) >= 5:
    print("correct guess✅")
else:
    print("too low repeat again🚨")
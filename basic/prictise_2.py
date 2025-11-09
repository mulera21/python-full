#logic
#number guessing game
print("Welcome to the number guessing game")
print("Guess a number between 0 and 20")
print("------------------------------------------")

secrete_number = 15

#logic to check the number
min = 1
max = 20
for i in range(6):
    print(f"attempts left:, {i+1}/6")

    user_1 = int(input("ENTER a number  "))

    if user_1 < min or user_1 > max:
        print("out of range🚨incorrect number")
    elif user_1 == secrete_number:
        print("correct guess✅")
        break
    elif user_1 > secrete_number:
        print("too high repeat again😒🚨")
    else:
        print("too low repeat again🚨")
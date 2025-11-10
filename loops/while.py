#while loop
# This program calculates the ticket price based on the user's age.
print("Welcome to the ticket price calculator!")
print("Please enter your age to determine your ticket price.")
print("-" * 40)

ticket_price = 200

while True :
    age = int(input("Enter your age: "))
    if age < 3 :
        print("Your ticket is free!")
        break
    elif age <= 12 :
        print(f"Your ticket price is ${ticket_price / 2}")
        break
    else :
        print(f"Your ticket price is ${ticket_price}")
        break
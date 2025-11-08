# Dictionary to store item quantities
#😒😒
print("--" * 50)

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

#adding a new contact
phonebook["David"] = "444-444-4444"
phonebook["edward"] = "333-333-3333"
print("Phonebook after adding contacts:", phonebook)

number = phonebook["Alice"]
print(f"📞📞calling Alice....({number})")


#advanced dictionary
print("--" * 50)
player = {"name" : "edmond",
          "class": "warrior",
          "level": 5,
          "health": 100,
            "Backpack":[]
            }

player["level"] += 1  #level up
player["health"] -= 20  #took damage

#adding items to backpack
player["Backpack"].append("Sword")
player["Backpack"].append("Shield")


for key, value in player.items():
    print(f"{key}: {value}")
          
          
         

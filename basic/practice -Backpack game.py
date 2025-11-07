# Backpack Game
# A simple text-based backpack game where the player can add, remove, and view items in their backpack.
# starting with an empty backpack.
backpack = []
print("0. starting journey with an empty backpack.")


print("🚨", backpack)
print("--" * 50)
print("1 . 😒picking up starterkit(Armor, shild, sword, potion).")
backpack.append("Armor")
backpack.append("Shield")
backpack.append("Sword")
backpack.append("Potion")
print("🚨", backpack)

# loot a tresure chest
print("--" * 50)
print("2 . 😍looting a treasure chest (Gold, Gem, Map).")

chest = ["Gold", "Gem", "Map"]
backpack.extend(chest)
print("🚨", backpack)
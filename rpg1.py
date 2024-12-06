'''
Exercise 3: Create a simple RPG game where the player's character has health points (HP) and can encounter monsters. 
Use conditional statements to simulate battles.
'''
player_hp = 100
monster_hp = 50

print("Welcome to the RPG game!")
print(f"Player HP: {player_hp}")
print(f"Monster HP: {monster_hp}")

action = input("Enter your action (attack/flee): ")

if action.lower() == "attack":
    damage = 20
    monster_hp -= damage
    print(f"You attacked the monster and dealt {damage} damage!")
    print(f"Monster HP: {monster_hp}")
else:
    print("You fled the battle.")

if monster_hp <= 0:
    print("Congratulations! You defeated the monster!")
else:
    print("The monster defeated you. Game over.")

#FYI
'''
lower() is a method is a method used to convert all the characters in a string to lowercase. 
It's commonly used to make string comparisons case-insensitive, 
as it transforms all characters to their lowercase representations.
'''

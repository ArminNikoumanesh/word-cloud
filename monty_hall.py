
import random

A = "A"
B = "B"
C = "C"

doors = ["A", "B", "C"]

prize = random.choice(doors)

selection = input("Select door 'A', 'B', or 'C': ")


if selection == prize:
        remaining = list(set(doors) - set(prize))
        open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
        alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))

else:
        open_door = random.choice(list(set(doors) - set(selection) - set(prize)))
        alternate = random.choice(list(set(doors) - set(open_door) - set(selection)))

print(f'Door {open_door} Was boz')
second_chance = input("Would you like to select the third door? Type 'Yes' or 'No': ")

if second_chance == "Yes":
        print (f""" The door you will switch to is: {alternate}""")

        if alternate == prize:
                print (f"""
                Congrats, you win! The prize was behind the alternate, {alternate}""")
        else:
                print (f"""
                Sorry, the prize was behind the original door {prize}""")


if second_chance != "Yes":
        print (f"""
        You decided to keep your initial door, {selection}""")
        if selection != prize:
                print (f"""
                Sorry, the prize was behind the alternate door, {prize}""")
        else:
                print (f"""
                Congrats, you win! The prize was behind your original selection, {selection}""")


print ("""
This is a check:""")

print (f"Prize: {prize}")
print (f"Selection: {selection}")
print (f"Alternate: {alternate}")
print (f"Door opened: {open_door}")
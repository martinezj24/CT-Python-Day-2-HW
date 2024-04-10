#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
         print("You found a boat!")
 #Task 2: Setting the Scene

if place == "cave":
    action = input('You enter the cave, light a torch or proceed in the dark?')
    if action == "light a torch":
        print("You found gold!")
    elif action == "proceed in the dark":
        print("You bump your head and pass out")
else:
    pass #Task 3: Default Path
name = input("What is your name?: ")
print("Hi " + name + ". Welcome to the game world.")
go = True
alive = True
sword = False

while go:
    door = input("You must choose between two doors - left and right: ")
    if door == "left":
        print("You enter an empty room.")
        if sword == True:
            print("You've already explored here. It's time to go back.")
            continue
        choice = input("Type 'explore' to look around or 'leave' to go back: ")
        if choice == "leave":
            continue
        else:
            print("You find a sword!")
            take_sword = input("Type 'take' to take the sword, or 'leave' to leave it behind: ")
            if take_sword == "take":
                sword = True
                print("You grab the sword and exit the room from where you came.")
                continue
            else:
                print("You leave the sword behind and exit the room from where you came.")
            continue
    else:
        print("You enter a room with a dragon!")
        choice = input("Type 'attack' to attack the dragon or 'leave' to go back: ")
        if choice == "leave":
            continue
        else:
            if sword == True:
                print("Your sword pierces the dragon's armour!")
                print("The dragon is dead - you win!")
                break
            else:
                print("Without a weapon, you quickly die.")
                print("You are dead - game over.")
                break

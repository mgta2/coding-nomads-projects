def magic():
    with open("magic.txt", "w") as file_out:
        my_str = "Book of Spell(s):\n"
        my_str += "--- 'fus ro dah'"
        file_out.write(my_str)
    return

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
            print("You've already explored here, but this time you see something new!")
            print("It's a strange-looking book called 'magic.txt'.")
            print("Unfortately the book cannot be opened in the game interface.")
            print("If only you could find out what's inside, it may help your quest...")
            magic()
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
        elif choice == "fus ro dah":
            print("Your magic words impress the beast, and it becomes your best friend.")
            print("In time, you become lovers.")
            print("You win!")
            break
        else:
            if sword == True:
                print("Your sword pierces the dragon's armour!")
                print("The dragon is dead - you win!")
                break
            else:
                print("Without a weapon, you quickly die.")
                print("You are dead - game over.")
                break

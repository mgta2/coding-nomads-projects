# Dragon Game V4
# Take Dragon Game v3 and add another API.

import requests # Requires venv to be running
import random

def cocktail_ingred():
    n = random.randint(0,400)
    my_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid={n}"
    response = requests.get(my_url).json()
    my_ingred = response['ingredients'][0]['strIngredient']
    ingred_descr = response['ingredients'][0]['strDescription']
    print("Despite leaving the sword behind, you're in luck!")
    print("You've found some", my_ingred)
    print("(In case you don't know: ", ingred_descr, ")")
    return

def get_name(length):
    if length<2:
        return_name = "X"
    elif length>40:
        return_name = "Sir Long Name IV"
    else:
        # Could implement an internet connnection check here. More info at:
        # https://www.kite.com/python/answers/how-to-check-internet-connection-in-python
        api_url = f"https://uzby.com/api.php?min={length}&max={length}"
        response = requests.get(api_url)
        return_name = response.text
    return return_name

def magic():
    with open("magic.txt", "w") as file_out:
        my_str = "Book of Spell(s):\n"
        my_str += "--- 'fus ro dah'"
        file_out.write(my_str)
    return

name = input("What is your name?: ")
print("Hi " + name + ". Welcome to the game world.")

api_name = get_name(len(name))
print("Your game character is called", api_name)

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
                cocktail_ingred()
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

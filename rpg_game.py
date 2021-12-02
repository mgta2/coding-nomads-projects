# RPG Project v2 (with inheritance)

import random

class Hero():
    
    def __init__(self, level, has_sword, has_bow):
        self.level = 1
        self.has_sword = False
        self.has_bow = False
        self.has_armour = False

class Opponent():
    
    def __init__(self, name, level, ranged):
        self.name = name
        self.level = level
        self.ranged = ranged
        
    def __str__(self):
        my_str = f"The monster is a level {self.level} foe."
        return my_str
    
    def attack(self, other, weapon): # other will always be of Hero class.
        level_sum = self.level + other.level
        if weapon == "bow" and self.ranged == True and not(self.name == "Dragon"):
            winner = "player"
        elif weapon == "sword" and self.ranged == False:
            winner = "player"
        else:
            n = random.randint(1,level_sum)
            if n <= self.level:
                winner = "monster"
            else:
                winner = "player"
        
        if winner == "player":
            other.level += self.level
            print("You win the battle!")
            print(f"Experience gained - you are now level {other.level}.")
        else:
            print("You lose the battle...")
            if weapon == "sword":
                other.has_sword = False
                print("You escape with you life but lose your sword while running away.")
            elif weapon == "bow":
                other.has_bow = False
                print("You manage to escape with your life, but your bow is destroyed in the chaos.")
            else:
                print("Unarmed, your death comes swiftly.")
                other.level = 0
        return winner

class WeakOpponent(Opponent):
    def attack(self, other, weapon):
        level_sum = self.level + other.level
        if weapon == "bow" and self.ranged == True and not(self.name == "Dragon"):
            winner = "player"
        elif weapon == "sword" and self.ranged == False:
            winner = "player"
        else:
            n = random.randint(1,level_sum)
            # Make it more likely to win when righting with no weapon.
            if n <= self.level/2:
                winner = "monster"
            else:
                winner = "player"
        
        if winner == "player":
            other.level += self.level
            print("You win the battle!")
            print(f"Experience gained - you are now level {other.level}.")
        else:
            print("You lose the battle...")
            if weapon == "sword":
                other.has_sword = False
                print("You escape with you life but lose your sword while running away.")
            elif weapon == "bow":
                other.has_bow = False
                print("You manage to escape with your life, but your bow is destroyed in the chaos.")
            else:
                print("Unarmed, your death comes swiftly.")
                other.level = 0
        return winner
        

class Boss(Opponent):
    # Code for the Dragon boss.
    def __init__(self, name, level, ranged, necro_orc_dead):
        # Add dialogue depending on whether the Necro and Orc are dead.
        super().__init__(name, level, ranged)
        self.necro_orc_dead = necro_orc_dead
    
    def __str__(self):
        my_str = "WARNING - BOSS MONSTER\n"
        if self.necro_orc_dead == False:
            my_str += "Monster's details are hidden while more foes remain in other rooms."
        else:
            my_str += f"The monster is a level {self.level} foe."
        return my_str
    
    def attack(self, other, weapon):
        # Make the fight 'harder' if you have both a bow and sword.
        self.level += 5*(other.has_bow + other.has_sword)
        level_sum = self.level + other.level
        n = random.randint(1,level_sum)
        if n <= self.level:
            winner = "monster"
        else:
            winner = "player"
        if winner == "player":
            other.level += self.level
            print("You win the battle!")
            print(f"Experience gained - you are now level {other.level}.")
        else:
            print("You lose the battle...")
            if weapon == "sword":
                other.has_sword = False
                print("You escape with you life but lose your sword while running away.")
            elif weapon == "bow":
                other.has_bow = False
                print("You manage to escape with your life, but your bow is destroyed in the chaos.")
            else:
                print("Unarmed, your death comes swiftly.")
                other.level = 0
        return winner

def choose_weapon(bow, sword):
    # Code to see what weapons hero has and select one to equip.
    if bow == True and sword == True:
        print("You have both a bow and a sword at your side.")
        user_input = input("By default you equip the sword; type 'bow' if instead you want the bow: ")
        if user_input.lower() == "bow":
            weapon_choice = "bow"
            print("You equip the bow, ready for a fight.")
        else:
            weapon_choice = "sword"
            print("You unsheath your sword.")
    elif bow == True:
        print("You equip your trusty bow.")
        weapon_choice = "bow"
    elif sword == True:
        print("You pull out your sword...")
        weapon_choice = "sword"
    else:
        print("With no weapon, you can do no more than raise your fists...")
        weapon_choice = "fists"
    
    return weapon_choice

hero = Hero(1, False, False)
necro_dead = False
orc_dead = False

flag = True
while True:
    print()
    if hero.level == 0:
        print("--- Game Over ---")
        break
    if flag == True:
        print("You wake up in a dimly lit room, no idea how you got there.\n"
              "Around the walls are closed doors labelled 1 to 5."
              )
        flag = False
    else:
        print("You have returned to the first room, the doors lie before you once again.")
    
    user_input = int(input("Pick a door number: "))
    
    if user_input == 1:
        # Final Boss.
        if necro_dead == True and orc_dead == True:
            necro_orc_dead = True
        else:
            necro_orc_dead = False
        
        dragon = Boss("Dragon", 10, True, necro_orc_dead)
        
        print("You see a giant dragon before you!")
        print("Busy looking at its treasure, the beast doesn't see you.")
        
        user_input = input("Type 'attack', 'inspect' or 'leave': ")
        
        if user_input.lower() == "attack":
            weapon = choose_weapon(hero.has_bow, hero.has_sword)
            winner = dragon.attack(hero, weapon)
            if winner == "player":
                print("You win the game!")
                break
            else:
                continue
        elif user_input.lower() == "inspect":
            print("You inspect the monster before you...")
            print(dragon)
            print("You are spotted and have to run out of the room before the monster attacks!")
            continue
        else:
            print("You leave the room.")
            continue
        
    elif user_input == 2:
        # Bow Room. Can take or leave. If take, you practice some shots and level up.
        if hero.has_bow == False:
            print("With a great shove door 2 swings aside.\n"
                  "In the corner of the room lies a bow, with a full quiver of arrows."
                  )
            user_input = input("Type 'take' to take the bow, else leave the room: ")
            if user_input.lower() == "take":
                hero.has_bow = True
                print("You spot a big red target poster on the other side of door 2."
                      "After a few practice shots, you feel comfortable wielding this weapon."
                      )
                hero.level += 1
                print("Level up! You are now level", hero.level)
                continue
            else:
                print("You leave the room. door two swings shut behind you.")
                continue
        else:
            print("The bow at your side, there's nothing more for you in room 2.")
            continue
    elif user_input == 3:
        # Non-ranged monster. Can attack, inspect, or leave.
        necro = Opponent("Necromancer", 7, False)
        
        print("You see an evil wizard - a necromancer!")
        print("It seems you entered the room without drawing his attention.")
        
        user_input = input("Type 'attack', 'inspect' or 'leave': ")
        
        if user_input.lower() == "attack":
            weapon = choose_weapon(hero.has_bow, hero.has_sword)
            winner = necro.attack(hero, weapon)
            if winner == "player":
                print("You leave the dead necromancer behind you as you exit the room.")
                necro_dead = True
                continue
            else:
                continue
        elif user_input.lower() == "inspect":
            print("You inspect the monster before you...")
            print(necro)
            print("You are spotted and have to run out of the room before the monster attacks!")
            continue
        else:
            print("You leave the room.")
            continue
        
    elif user_input == 4:
        # Ranged monster with sword (Orc). Win sword if victorious.
        orc = WeakOpponent("Orc", 3, True)
        
        print("Pushing open the door, you see a massive Orc before you, wielding a sword.")
        print("Luckily the monster didn't notice you entering...")
        
        user_input = input("Type 'attack', 'inspect' or 'leave': ")
        
        if user_input.lower() == "attack":
            weapon = choose_weapon(hero.has_bow, hero.has_sword)
            winner = orc.attack(hero, weapon)
            if winner == "player":
                print("The orc lies dead. You take its sword, victorious.")
                hero.has_sword = True
                orc_dead = True
                continue
            else:
                continue
        elif user_input.lower() == "inspect":
            print("You inspect the monster before you...")
            print(orc)
            print("You are spotted and have to run out of the room before the monster attacks!")
            continue
        else:
            print("You leave the room.")
            continue
        
    else:
        # Sword practice room (level up x2 if practice with sword).
        print("You push open door 5 to find a fully equipped sword-training workshop.")
        if hero.has_sword == False:
            print("With no sword, there's nothing in here for you.")
            continue
        else:
            user_input = input("Type 'train' to train up your skills, else leave: ")
            if user_input.lower() == "train":
                hero.level += 2
                print(f"Your level has increased to {hero.level}!")
                print("Exhausted from your hard work, you leave the room.")
                continue
            else:
                print("You leave the training workshop behind you.")
                continue

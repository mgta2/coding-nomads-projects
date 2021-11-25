# Rock-Paper-Scissors Game

import random

def get_hand(n):
    if n == 0:
        answer = "scissors"
    elif n == 1:
        answer = "rock"
    else:
        answer = "paper"
    return answer

def determine_winner(user_choice, machine_choice):
    winner = "you!"
    if user_choice == machine_choice:
        winner = "no one!"
    else:
        if user_choice == "scissors" and machine_choice == "rock":
            winner = "the machine."
        elif user_choice == "rock" and machine_choice == "paper":
            winner = "the machine."
        elif user_choice == "paper" and machine_choice == "scissors":
            winner = "the machine."
    return winner

go = False
user_input = input("Enter 0 for scissors, 1 for rock, and 2 for paper: ")
if user_input.isdigit():
    user_input = int(user_input)
    if user_input in [0, 1, 2]:
        go = True
    else:
        print("You did not enter 0, 1, or 2.")
else:
    print("You did not enter an integer")

machine_input = random.randint(0,2)
user_choice = get_hand(user_input)
machine_choice = get_hand(machine_input)

print("You chose", user_choice)
print("The machine chose", machine_choice)
print("The winner is:", determine_winner(user_choice, machine_choice))

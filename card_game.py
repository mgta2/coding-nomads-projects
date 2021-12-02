# Card Game Project

import numpy

class Hand():
    
    def __init__(self, my_list):
        self.cards = my_list
    
    def __str__(self):
        return str(self.cards)
    
    def swap(self, other, index):
        # Self is hand.
        # Other is pile.
        # Index is which of user's cards we swap (1,...,7).
        new_hand = []
        new_pile = other.cards[:44]
        for i in range(0,7):
            if i != index-1:
                new_hand.append(self.cards[i])
            else:
                new_hand.append(other.cards[-1])
        new_pile.append(self.cards[index-1])
        self.cards = new_hand
        other.cards = new_pile

def convert(n):
    if n//13 == 0:
        # Heart
        if n == 0:
            output = "H13"
        else:
            output = "H"+f"{n}"
    elif n//13 == 1:
        # Diamond
        if n == 13:
            output = "D13"
        else:
            output = "D"+f"{n-13}"
    elif n//13 == 2:
        # Spade
        if n == 26:
            output = "S13"
        else:
            output = "S"+f"{n-26}"
    else:
        # Club
        if n == 39:
            output = "C13"
        else:
            output = "C"+f"{n-39}"
    return output

def run_checker(my_str, hand):
    # my_str is user run choices.
    # hand is current user hand as a list.
    
    # First we reorder the hand list to get the selection.
    selection = []
    for i in range(0,7):
        selection.append(hand[int(my_str[i])-1])
    
    run_three = selection[:3]
    run_four = selection[3:]
    
    three_run = []
    for x in run_three:
        three_run.append(convert(x))
    four_run = []
    for x in run_four:
        four_run.append(convert(x))
    
    print(three_run)
    print(four_run)
    
    # Check if first 3 is a run:
    three_is = False
    if three_run[0][1:] == three_run[1][1:] and three_run[1][1:] == three_run[2][1:]:
        # Have e.g. H2, D2, S2
        three_is = True
    elif three_run[0][0] == three_run[1][0] and three_run[1][0] == three_run[2][0]:
        # Need check if consecutive.
        if int(three_run[0][1:]) + 1 == int(three_run[1][1:]) and int(three_run[1][1:]) + 1 == int(three_run[2][1:]):
            three_is = True
    
    #Check if last 4 is a run:
    four_is = False
    if four_run[0][1:] == four_run[1][1:] and four_run[1][1:] == four_run[2][1:] and four_run[2][1:] == four_run[3][1:]:
        # Have e.g. H3, D3, S3, C3
        four_is = True
    elif four_run[0][0] == four_run[1][0] and four_run[1][0] == four_run[2][0] and four_run[2][0] == four_run[3][0]:
        # Need check if consecutive.
        if int(four_run[0][1:]) + 1 == int(four_run[1][1:]) and int(four_run[1][1:]) + 1 == int(four_run[2][1:]) and int(four_run[2][1:]) + 1 == int(four_run[3][1:]):
            four_is = True
    
    # If both three_is and four_is are True then we're good.
    if three_is == True and four_is == True:
        output = True
    else:
        output = False
    return output

n = numpy.random.permutation(52) # Gives random reordering of [0, 1, ..., 51]
my_list = []
for element in n:
    my_list.append(element)
n = my_list
pile = Hand(n[:45])
hand = Hand(n[45:])

# Now user interface

moves = 0

while True:
    
    moves += 1
    pile_card = convert(pile.cards[-1])
    
    # Users's 7 and the pile's top card.
    print(f"Top card of the pile: {convert(pile.cards[-1])}")
    print()
    print(f"Your cards: {convert(hand.cards[0])}, "
          f"{convert(hand.cards[1])}, "
          f"{convert(hand.cards[2])}, "
          f"{convert(hand.cards[3])}, "
          f"{convert(hand.cards[4])}, "
          f"{convert(hand.cards[5])}, "
          f"{convert(hand.cards[6])}, "
          )
    
    # User input: swap, run or discard.
    user_input = input("Do you want to 'swap', 'discard' or enter a 'run': ")
    
    if user_input == "swap":
        # Which card do you want to swap?
        user_input = int(input("Which number card do you want to swap (1,...7): "))
        hand.swap(pile, user_input)
        
    elif user_input == "discard":
        # Permute the pile.
        new_pile = [pile.cards[-1]]
        for i in range (1,45):
            new_pile.append(pile.cards[i-1])
        pile = Hand(new_pile)
        
    else:
        # Enter your run in the form (3-run)(4-run)
        # Call function to give true or false.
        # If true, break out of the loop, else print message and 'continue'.
        my_str = "Enter your 3-run followed by your 4-run as a 7-tuple (e.g. 3127546): "
        user_input = input(my_str)
        outcome = run_checker(user_input, hand.cards)
        
        if outcome == True:
            print(f"Congratulations! You have won in {moves} moves.")
            break
        else:
            print("That wasn't a valid run. The game continues...")
    print("----------------------")

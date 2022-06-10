from logging import raiseExceptions
from pickle import FALSE, TRUE
import random


game = ["Rock", "Scissors", "Paper"]

# When the program is run, ask the user to pick an option between "R", "P" or "S"
# Rock(fist) beat scissors(pointers)
# scissors(pointers) beat paper(flat hands)
# paper(flat hands) beats rock(fist)

print("Select:\n")
user = input("Select one of these-(Rock, Scissors, OR Paper): ")
CPU = random.choice(game)

print(f"Your user input is {user}, while the computer input is {CPU} \n")


if user not in game:
    print("There has been an error in your input, try again with the right input!")

elif user == "Rock":
    if CPU == "Scissors":
        print(f"Player({user.title()}): Computer({CPU.title()})")
        print("Rock beats SCISSORS")
    else:
        print("paper beats rocks, you lose")

elif user == "Scissors":
    if CPU == "Paper":
        print(f"Player({user.title()}): Computer({CPU.title()})")
        print("Scissors beat PAPER")
    else:
        print("Rock beats Scissors")

elif user == "Paper":
    if CPU == "Rock":
        print(f"Player({user.title()}): Computer({CPU.title()})")
        print("Paper beats Rock")

done = True
while done:
    if user == CPU:
        print(
            f"you both chose {user} as values, you have a tie, start over again")


"""for user in game:
    user = input("select either 'R'or 'S' or 'P':  ")
for comp in game:
    comp = random.choice(game)
    print(comp)
    
    
    if user not in game:
        print("You inputed a wrong answer")



if comp == user:
    print(f"Computer and Player Chose the same")"""

"""for user in game:
        if user not in game:
            print("you selected the wrong letter ")
        elif user in game:
            print(f"you selected {user} the first time")
    else:
        print("Start all over again")"""


"""while True:
    for item in fig:
        if item == "R":
            print("You chose rock, You rock!")
        else:
            item == "S"
            print("you chose a scissor")

        else
"""

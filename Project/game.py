player_name = input("State your name: ")
player_age = int(input("State your age: "))
game_name = ("unknown")

import random


if player_age < 12:
    print("You are too young to play this game.")
if player_age >= 12:
    print(("Your name: ") + str(player_name))
    print(("your age: ") + str(player_age))
    print("")
    print(f"Welcome {player_name} to {game_name}, you can enter prompted commands to play the game, or if you would like to quit at any time, type 'lopeta'.")
    print("")


def begin_game():
    beginning = input("You stand atop a cliff, do you, 'jump', or 'turn back'? ")
    if beginning == "jump":
        print("why would you do that? You died..")
        print("")
        print("Lets start over:")
        print("")
        begin_game()
    elif beginning == "turn back":
         print("you turn back, returning to the shack. " \
        "You sit on the chair and look at what is on the table: " \
        "an axe, a water bottle, and a hat.")
    else:
        print("that is not a valid command, please try again")
        print("")
        beginning = input("You stand atop a cliff, do you, 'jump', or 'turn back'? ")





if player_age >= 12:
    begin_game()
    
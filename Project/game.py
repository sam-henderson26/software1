import random

player_name = input("State your name: ")
player_age = int(input("State your age: "))
game_name = ("The Lumberjack")

player_inventory = {
    "Axe": 1,
    "Gold": 0,
    "Wood": 0
}

# Game areas:
def begin_game():    
    beginning = input("You look into the forest, focusing on the amalgamation of roots covering the exit, do you 'attack' the roots or 'go home'? ")
    if beginning == "attack":
        print("")
        print("You have no way of breaking through them, yet still, you try, and your hands hurt after trying.")
        print("")
        print("Lets try this again:")
        print("")
        begin_game()
    elif beginning == "go home":
        print("")
        print("you turn back, returning to your makeshift shack. ")
        print("You sit on the chair and look at what is on the table: ")
        print("an axe, and a coin purse. ")
        print("You take both: ")
        print("You can now view your inventory with 'i'")
        after_shack()
    else:
        print("")
        print("that is not a valid command, please try again")
        print("")
        begin_game()

def after_shack():
    print("You now break through the roots with ease, travelling in towards the dense, packed forest")
    print("The path forks ahead, to your left, a clearing with some smaller, lighter trees; to your right, the forest remains dense and and difficult to navigate.")
    choice1 = input("Do you travel 'left' or 'right'? You can view your inventory wiht 'i'.")
    if choice1 == "left":
        input("These trees look like your axe could handle them, will you try to cut them down ('y/n') ? ")
        if "y":
            print("You chopped down the smallest tree, the only one your axe could handle,")
            print("as it fell, a bird's nest fell with it, destroying the bird's home.")
            # roll random number between 1-5 (due to having only boring axe) to see how much wood the player receives.
            # add wood to inventory
            print("With the wood in your bag, you now backtrack and travel down the dark path.")
            #add next area and decisions.
        if "n":
            print("There is nothing else to do here, you backtrack and go down the dark path instead.")
    elif choice1 == "right":
        print("You decide to continue down the spiralled darker path, holding your axe close as the light struggles to penetrate the woodland.")
        # add next area and decisions.
    elif choice1 == "i":
        # add inventory in here.
        print(player_inventory)
    else:
        print("")
        print("that is not a valid command, please try again")
        print("")
        after_shack()

# Main menu:
def rules():
    while True:
        print("")
        print("Each move is made by choosing one of two options, this is done by typing one of those actions.")
        print("Sometimes you will have an opportunity to add things to your inventory, don't miss these!")
        print("Get to the end by finding the correct route whilst building up your inventory value as much as possible.")
        print("")
        return_to_main_menu = input("Type 'back' to return to the main menu: ")
        if return_to_main_menu == "back":
            break
        else:
            print("Please type 'back', to return to the main menu.")

def quit_game():
    print("Thank you for trying the game!")
    exit()
    
def main_menu():
    while True:
        print("The Lumberjack")
        print("'1': Begin Chopping")
        print("'2': Rules")
        print("'3': Quit game")
        main_menu_choice = input("Please choose an option: ")
        if main_menu_choice == "1":
            begin_game()
        if main_menu_choice == "2":
            rules()
        if main_menu_choice == "3":
            quit_game()
        else:
            print("Please type 1, 2, or 3.")


if player_age < 12:
    print("You are too young to play this game.")
if player_age >= 12:
    print(("Your name: ") + str(player_name))
    print(("your age: ") + str(player_age))
    print("")
    print(f"Welcome {player_name}!")
    main_menu()

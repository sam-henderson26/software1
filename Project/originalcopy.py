

# copy of code before changing the functioned areas into dictionary. # No longer used..



import random

class Area:
    def __init__(self, name, description, action):
        self.name = name
        self.description = description
        self.action = action

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = {
    "Axe": 1,
    "Gold": 0,
    "Wood": 0
}

user_name = input("State your name: ")
player_age = int(input("State your age: "))
game_name = ("The Lumberjack")

if player_age < 12:
    print("You are too young to play this game.")

user = Player(name = user_name, location = "main_menu")

print(f"Your name: {user.name}")
print(f"your age: {player_age}")
print("")
print(f"Welcome {user.name}!")

# Game areas:

def begin_game(player):
    while  True:
        beginning = input("You look into the forest, focusing on the amalgamation of roots covering the exit, do you 'attack' the roots or 'go home'? ")
        if beginning == "attack":
            print("")
            print("You have no way of breaking through them, yet still, you try, and your hands hurt after trying.")
            print("")
            print("Lets try this again:")
            print("")

        elif beginning == "go home":
            print("")
            print("you turn back, returning to your makeshift shack. ")
            print("You get home, and pick up the items from the table: an axe, and a coin purse, putting them into your backpack.")
            print("You can now view your inventory with 'i'")
            break
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")
    after_shack(player)

def after_shack(player):
    print("You now break through the roots with ease, travelling in towards the dense, packed forest")
    print("The path forks ahead, to your left, a clearing with some smaller, lighter trees; to your right, the forest remains dense and difficult to navigate.")
    while True:
        choice1 = input("Do you travel 'left' or 'right'? inventory 'i'. ")
        if choice1 == "left":
            while True:
                choice2 = input("These trees look like your axe could handle them, will you try to cut them down ('y/n') ? ")
                if choice2 == "y":
                    print("You chopped down the smallest tree, the only one your axe could handle,")
                    print("as it fell, a bird's nest fell with it, destroying the bird's home.")
                    axe1_roll = random.randint(1,3)
                    print(f"The tree produced {axe1_roll} wood.")
                    player.inventory["Wood"] += axe1_roll
                    print("With the wood in your bag, you now backtrack and travel down the dark path.")
                    dark_path(player)
                    return
                elif choice2 == "n":
                    print("There is nothing else to do here, you backtrack and go down the dark path instead.")
                    dark_path(player)
                    return
                else:
                    print("")
                    print("that is not a valid command, please try again")
                    print("")            
            
        elif choice1 == "right":
            dark_path(player)
            return
            
        elif choice1 == "i":
            print("")
            print(player.inventory)
            print("")
        
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")

def dark_path(player):
    print("The roots tighten around the pathway, the atmosphere gets darker and the air gets heavy...")
    print("You see the silhouette of a structure to the left, and a huddle of trees awaiting chopping to the right.")
    while True:
        choice3 = input("Do you head 'left' or 'right'? ")
        if choice3 == "left":
            print("You head into the fog and towards the structure; as it comes clearer into view, you see a lady buying wood:")
            while True:
                choice4 = input("'Would you like to sell your logs to me? I'll pay you 2 coins for every log!' she states. (y/n): ")
                if choice4 == "y":
                    print("You hand over your logs and she gives you some coins.")
                    player.inventory["Gold"] += (player.inventory["Wood"] * 2)
                    player.inventory["Wood"] = 0
                    print(player.inventory)
                    #next area
                    return
                elif choice4 == "n":
                    print("You decide to not sell your logs to the lady.")
                    #next area
                    return
                else:
                    print("")
                    print("that is not a valid command, please try again")
                    print("")

        elif choice3 == "right":
            # do this side of the choice next
            return




# Main menu:
def rules(player):
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

def quit_game(player):
    print("Thank you for trying the game!")
    exit()
    
def main_menu(player):
    while True:
        print("The Lumberjack")
        print("'1': Begin Chopping")
        print("'2': Rules")
        print("'3': Quit game")
        main_menu_choice = input("Please choose an option: ")
        if main_menu_choice == "1":
            begin_game(player)
            return
        if main_menu_choice == "2":
            rules(player)
        if main_menu_choice == "3":
            quit_game(player)
            return
        else:
            print("Please type 1, 2, or 3.")


if player_age < 12:
    print("You are too young to play this game.")
if player_age >= 12:
    print(f"Your name: {user.name}")
    print(f"your age: {player_age}")
    print("")
    print(f"Welcome {user.name}!")

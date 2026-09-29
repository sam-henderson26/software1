import random

# CLASSES:

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

# ENTRANCE TO MAIN MENU:

user_name = input("State your name: ")
player_age = int(input("State your age: "))
game_name = ("The Lumberjack")

if player_age < 12:
    print("You are too young to play this game.")
    exit()

user = Player(name = user_name, location = "main_menu")

print(f"Your name: {user.name}")
print(f"your age: {player_age}")
print("")
print(f"Welcome {user.name}!")

# GAME DECISIONS:

# (MAIN MENU OPTIONS):
def main_menu_start(player):
    while True:
        print("'1': Begin Chopping")
        print("'2': Rules")
        print("'3': Quit game")
        main_menu_choice = input("Please choose an option: ")
        if main_menu_choice == "1":
            return "begin_game"
        elif main_menu_choice == "2":
            return "rules"
        elif main_menu_choice == "3":
            return "quit_game"
        else:
            print("Please type 1, 2, or 3.")

def rules_start(player):
    while True:
        return_to_main_menu = input("Type 'back' to return to the main menu: ")
        if return_to_main_menu == "back":
            return "main_menu"
        else:
            print("Please type 'back', to return to the main menu.")

def quit_game_start(player):
    print("Thank you for trying the game!")
    exit()


# START OF GAME AND OPTIONS:

def begin_game_start(player):
    while  True:
        beginning = input("Do you try to 'attack' the roots or 'go home'? ")
        if beginning == "attack":
            print("You have no way of breaking through them, yet still, you try, and your hands hurt after trying.")
            print("Lets try this again:")
            print("")
        elif beginning == "go home":
            print("you turn back, returning to your makeshift shack. ")
            print("You get home, and pick up the items from the table: an axe, and a coin purse, putting them into your backpack.")
            print("You can now view your inventory with 'i'")
            return "after_shack"
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")

def after_shack_start(player):
    print("To your left you see a huddle of thin trees, and to your right, the path continues.")
    while True:
        choice1 = input("Do you travel 'left' or 'right'? (inventory 'i'): ")
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
                    return "dark_path"
                elif choice2 == "n":
                    print("There is nothing else to do here, you backtrack and go down the dark path instead.")
                    return "dark_path"
                else:
                    print("")
                    print("that is not a valid command, please try again")
                    print("")            
            
        elif choice1 == "right":
            return "dark_path"
            
        elif choice1 == "i":
            print("")
            print(player.inventory)
            print("")
        
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")

def dark_path_start(player):
    print("You see the silhouette of a structure to the left, and a huddle of trees awaiting chopping to the right.")
    while True:
        choice3 = input("Do you head 'left' or 'right'? ")
        if choice3 == "left":
            print("You head into the fog and towards the structure; as it comes clearer into view, you see a lady buying wood:")
            while True:
                choice4 = input("'Would you like to sell your logs to me? I'll pay you 2 coins for every log!' she states. (y/n): ")
                if choice4 == "y":
                    player.inventory["Gold"] += (player.inventory["Wood"] * 2)
                    print(f"You hand over {player.inventory["Wood"]} logs and she gives you {player.inventory["Gold"]} coins.")
                    player.inventory["Wood"] = 0
                    print(player.inventory)
                    #next area
                    return
                elif choice4 == "n":
                    print("You decide to not sell your logs to the lady. And instead continue towards the fog.")
                    #next area
                    return
                else:
                    print("")
                    print("that is not a valid command, please try again")
                    print("")

        elif choice3 == "right":
            # do this side of the choice next
            return


    
# DICTIONARY OF AREAS (ROOMS):

area_map = {
    "main_menu": Area(
        name = "The Lumberjack",
        description = "Welcome to The Lumberjack!",
        action = main_menu_start
    ),
    "rules": Area(
        name = "Rules",
        description = "Decide your path by choosing directions 'left' or 'right', and actions 'y' or 'n'.",
        action = rules_start
    ),
    "quit_game": Area(
        name = "Quit Game",
        description = "Thank you for trying the game!",
        action = quit_game_start
    ),
    "begin_game": Area(
        name = "The Shack",
        description = "Looking out towards the forest, you see an amalgamation of roots covering any chance of an easy exit",
        action = begin_game_start
    ),
    "after_shack": Area(
        name = "Entrance to the Forest",
        description = "You break through the roots with measured ease, travelling in towards the densely packed forest",
        action = after_shack_start
    ),
    "dark_path": Area(
        name = "Dark Path",
        description = "The roots tighten around the pathway, the atmosphere gets darker and the air gets heavy...",
        action = dark_path_start
    ),
}


# MAKE THE GAME WORK AND UPDATES PLAYER LOCATION:

while True:
    area_place = user.location
    current_area = area_map[area_place]

    print("")
    print(f"{current_area.name}")
    print(current_area.description)
    
    next_area_place = current_area.action(user)
    user.location = next_area_place
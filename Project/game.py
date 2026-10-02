import random
import json
import os


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

class Item:
    def __init__ (self, name, description, multiplier = 1):
        self.name = name
        self.description = description
        self.multipler = multiplier


try:
    with open ("Project/intro.txt", "r")as my_file:
        file_data = my_file.read()
        print(file_data)
except FileNotFoundError as e:
    print ("File not found.")
except IOError as e:
    print ("An error has occurred.")
    print(e)

try:
    with open ("Project/instructions.txt", "r")as my_file:
        file_data = my_file.read()
        print(file_data)
        print("")
except FileNotFoundError as e:
    print ("File not found.")
except IOError as e:
    print ("An error has occurred.")
    print(e)



def save_game (player):
    save_data = {
        "name": player.name,
        "location": player.location,
        "inventory": player.inventory
    }
    with open("Project/save_game.json", "w") as file:
        json.dump(save_data, file)
    print("saved")


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
            return "lopeta"
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
    save_game(player)
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
    print("To your left you see a huddle of thin trees, and to your right, the path continues deeper into the forest.")
    while True:
        choice1 = input("Do you travel 'left' or 'right'? (inventory 'i'): ")
        if choice1 == "left":
            while True:
                choice2 = input("These trees look like your axe could handle them, will you try to cut them down? ('y/n') (i) ")
                if choice2 == "y":
                    print("You chopped down the smallest tree, the only one your axe could handle,")
                    axe1_roll = random.randint(1,3)
                    print(f"The tree produced {axe1_roll} wood.")
                    player.inventory["Wood"] += axe1_roll
                    print("With the wood in your bag, you now backtrack and travel down the dark path.")
                    return "dark_path"
                elif choice2 == "n":
                    print("There is nothing else to do here, you backtrack and go down the dark path instead.")
                    return "dark_path"
                elif choice2 == "i":
                    print("")
                    print(player.inventory)
                    print("")
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
        choice3 = input("Do you head 'left' or 'right'? (i) ")
        if choice3 == "left":
            print("You head into the fog and towards the structure; as it comes clearer into view, you see a lady buying wood:")
            while True:
                choice4 = input("'Would you like to sell your logs to me? I'll pay you 2 coins for every log!' she states. (y/n) (i) ")
                if choice4 == "y":
                    player.inventory["Gold"] += (player.inventory["Wood"] * 2)
                    print(f"You hand over {player.inventory["Wood"]} logs and she gives you {player.inventory["Gold"]} coins.")
                    player.inventory["Wood"] = 0
                    print(player.inventory)
                    print("You travel towards the fog.")
                    return "foggy_place"
                elif choice4 == "n":
                    print("You decide to not sell your logs to the lady. And instead continue towards the fog.")
                    return "foggy_place"
                
                elif choice4 == "i":
                            print("")
                            print(player.inventory)
                            print("")
                else:
                    print("")
                    print("that is not a valid command, please try again")
                    print("")

        elif choice3 == "right":
            print("After analysing the trees, you're confident you can cut down 3 of the trees.")
            while True:
                choice5 = input("Do you start swinging your axe? (y/n) (i) ")
                if choice5 == "y":
                    axe1_roll2 = random.randint(3,9)
                    print(f"The trees produced {axe1_roll2} wood.")
                    player.inventory["Wood"] += axe1_roll2
                    print(f"You now have {player.inventory["Wood"]}.")
                    print("After cutting down the trees, there is now a clearing, you see a deer to the left, and a pond to the right.")
                    choice6 = input("Do you follow the deer ('left') or walk to the pond ('right)? (i) ")
                    if choice6 == "left":
                        return "deer_trail"
                    elif choice6 == "right":
                        return "pond_area"
                    elif choice6 == "i":
                        print("")
                        print(player.inventory)
                        print("")
                    else:   
                        print("")
                        print("that is not a valid command, please try again")
                        print("")
                elif choice5 == "n":
                    print("You decide not to chop down the trees, walking round them, you see a squirrel and it's family living out of the trees.")
                    print("The squirrel is trying to show you something:")
                    choice7 = input("The squirrel offers you a way out of the forest, through a mysterious portal. Do you take the portal? (y/n) (i) ")
                    if choice7 == "y":
                        return "ending_friendly"
                    elif choice7 == "n":
                        choice8 = input("Looking into the forest, you see a deer to the left, and a pond to the right. (left/right) (i) ")
                        if choice8 == "left":
                            return "deer_trail"
                        elif choice8 == "right":
                            return "pond_area"
                    elif choice7 == "i":
                        print("")
                        print(player.inventory)
                        print("")
                    else:   
                        print("")
                        print("that is not a valid command, please try again")
                        print("")
                        if choice8 == "left":
                            return "deer_trail"
                        elif choice8 == "right":
                            return "pond_area"
                        elif choice8 == "i":
                            print("")
                            print(player.inventory)
                            print("")
                        else:   
                            print("")
                            print("that is not a valid command, please try again")
                            print("")
                elif choice5 == "i":
                    print("")
                    print(player.inventory)
                    print("")
                else:
                    print("")
                    print("that is not a valid command, please try again")
                    print("")
        elif choice3 == "i":
            print("")
            print(player.inventory)
            print("")
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")

def ending_friendly_start(player):
    print("The world looks beautiful. You look down and the squirrel is by your side:")
    print("This is your reward for caring about the forest and it's inhabitants. I thank you. We all thank you.")
    print("You feel joy and happiness, laying down your axe, you follow the squirrel into a relaxing life of calmness and begin meeting the other animals")    
    print("")
    print("You did not destroy the squirrel's home, and therefore were gifted the World of Life.")
    print("You have finished the game! You have recieved the friendly ending! I would be proud.")
    print("")
    return "main_menu"

def foggy_place_start(player):
    print("You walk with your hands ahead of you, feeling around. You keep bumping into thick, old, trees")
    while True:
        choice9 = input("Should you cut the trees down? (y/n) (i) ")
        if choice9 == "y":
            print("You start swinging your axe into every tree you come across, until your bag is struggling to close.")
            axe1_roll3 = random.randint(5, 15)
            print(f"The old trees produced {axe1_roll3} wood.")
            player.inventory["Wood"] += axe1_roll3
            print(f"You now have {player.inventory["Wood"]}.")
            print("After chopping down all the trees you see a bright light beaming through the fog.")
            print("The light leads to a portal, where a mysterious figure awaits, asking:")
            while True:
                choice10 = input("Would you sell me those logs, I would pay you handsomely indeed... (y/n) (i) ")
                if choice10 == "y":
                    player.inventory["Gold"] += (player.inventory["Wood"] * 2)
                    print(f"You hand over {player.inventory["Wood"]} logs and the mysterious stranger gives you {player.inventory["Gold"]} coins.")                        
                    player.inventory["Wood"] = 0
                    print(player.inventory)
                    print("The stranger points towards the portal, you walk through proudly clutching your new full bag of coins.")
                    return "ending_greed"
                elif choice10 == "n":
                    print("How about instead, I trade those logs you have for some seeds? But you must enter the portal. (y/n) (i) ")
                    print("You hand over all of your logs and the stranger returns to you a pouch of small seeds. You then do as he wishes.")
                    return "ending_rebuild"                       
                elif choice10 == "i":
                    print("")
                    print(player.inventory)
                    print("")
                else:                            
                    print("")
                    print("that is not a valid command, please try again")
                    print("")          

        elif choice9 == "n":
            pass
        elif choice9 == "i":
            print("")
            print(player.inventory)
            print("")
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")        

def deer_trail_start(player):
    print("The old man is herding every type of animal, from big to small, hairy to scaled, he is wondrous. The deer joins the herd.")
    while True:
        choice11 = input("He sees you and puts out his hand, seemingly asking for some gold. Will you? (y/n) (i) ")
        if choice11 == "y":
            print("You reach into your purse:")
            if player.inventory["Gold"] > 0:
                print("You hand him 1 gold coin.")
                player.inventory["Gold"] - 1
                print(f"You had {player.inventory["Gold"] + 1} coins, you now have {player.inventory["Gold"]} coins.")
                print(player.inventory)
                print("")
                print("The old shepherd thanks you and begins moving his hands in a wistful manner: A portal appears.")
                return "ending_kind"
            if player.inventory["Gold"] == 0:
                print("You try i find a coin in your purse but fail, as you have not cut down or maybe sold any trees.")
                print("The old man sees you tried to help him, he does not need a coin, but knows your intentions were true.")
                return "ending_kind"
        if choice11 == "n":
            print("You begin to lose consciousness as the old man starts waving his stick around you")
            return "ending_animal"
        elif choice11 == "i":
            print("")
            print(player.inventory)
            print("")
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")               

def pond_area_start(player):
    print("As you get to the pond there is a stranger in the pond reaching for air, they can't swim up!")
    while True:
        choice12 = input("You can't reach him on your own, but 1 log would help him survive, do you try? (y/n) (i) ")
        if choice12 == "y":
            if player.inventory["Wood"] > 0:
                print("You throw a log into the water and the stranger manages to grab it and stay afloat.")
                player.inventory["Wood"] - 1
                print("The pond begins to drain, the stranger gets sucked down and disappears.")
                print("Then you see the land around the pond begins to get sucked into the hole, you feel yourself being dragged in.")
                return "ending_kind"
            if player.inventory["Wood"] == 0:
                print("You have no wood in your bag, you watch helplessly, then decide to throw your bag down and jump in to save them!")
                print("Everything goes dark")
                return "ending_kind"

        elif choice12 == "n":
            print("You pay no attention and continue to the portal built up on the other side of the pond.")
            print("The sign reads: An unkind soul will not be allowed to live in happiness.")
            print("A strong force pushes you into the portal")
            return "ending_unkind"

        elif choice12 == "i":
            print("")
            print(player.inventory)
            print("")
        else:
            print("")
            print("that is not a valid command, please try again")
            print("")     

def ending_rebuild_start(player):
    print("You know what you must do, after destroying so much life in the forest, you have been challenged with creating")
    print("a whole new world full of life, starting with a small bag of seeds...")
    print("")
    print("You have finished the game! You have tasked your character with creating a world of life from nothing but a bag of seeds.")
    print("")
    return "main_menu"

def ending_greed_start(player):
    print("As you look down, still smiling, you soon realise what you're walking upon: rolling hills of unlimited gold coins!")
    print("You're rich! You begin throwing handfuls of coins around and dancing...")
    print("You run out of breath and begin to realise that, there really is an unlimited amount of coin here, but that is infact, all that is here...")
    print("")
    print("You have finished the game! Although your character is now stuck for eternity, with nothing to spend all that money on...")
    print("")
    return "main_menu"

def ending_kind_start(player):
    print("You feel thankful to hear the sounds of cars and buses, people talking and dogs barking")
    print("You see people you have memories of seeing before, places that you think you remember, are you back home?")
    print("")
    print("Congratulations! You have completed the game and your character was safely returned to their home!")
    print("")
    return "main_menu"

def ending_animal_start(player):
    print("You did not help the old man by giving him a coin, you regain consciousness as you're walking,")
    print("Looking around, you realise you're now trapped in a sea of animals constantly trapped walking, and walking, and walking, forever.")
    print("")
    return "main_menu"

def ending_unkind_start(player):
    print("You can't catch your breath, every time you reach up, you plunge back down, you can see the light above you, but below is darkness.")
    print("You can't give up, not now, not ever, I hope someone has more kindness than you did.")
    print("")
    print("You have completed the game! Maybe try playing again and finishing it differently next time?")
    print("")
    return "main_menu"



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
    "foggy_place": Area(
        name = "Foggy Place",
        description = "As you step into the thick fog, you feel the air become harder to breathe, and you struggle to see ahead of you.",
        action = foggy_place_start
    ),
    "deer_trail": Area(
        name = "Deer Trail",
        description = "You follow the deer trail, coming across a shepherd with a long walking stick.",
        action = deer_trail_start
    ),
    "pond_area": Area(
        name = "Pond",
        description = "You make your way to the pond, a nice green grass surrounds, and a portal with a sign across the pond awaits.",
        action = pond_area_start
    ),
    "ending_friendly": Area(
        name = "Life Ending",
        description = "You step into the portal, with a great blinding flash of light. When you open your eyes, you're surrounded by beautiful wilderness, animals and luscious greenery.",
        action = ending_friendly_start
    ),
    "ending_greed":Area(
        name = "Land of Gold",
        description = "You step down as the portal behind you vanishes abruptly, every step is like shingle on a beach.",
        action = ending_greed_start
    ),
    "ending_rebuild":Area(
        name = "Land of Promise",
        description = "You stand, as rain begins pouring down, looking, you see nothing around for as far as you can see.",
        action = ending_rebuild_start
    ),
    "ending_kind":Area(
        name = "Old World",
        description = "The portal leads to a city, a one that feels familiar.",
        action = ending_kind_start
    ),
    "ending_animal":Area(
        name = "Endless Wandering",
        description = "The old man looks at you with disappointed eyes, almost to say that was a test of generosity,",
        action = ending_animal_start
    ),
    "ending_unkind":Area(
        name = "Condemned",
        description = "You're reaching, trying to grab onto something, to pull yourself up, you just can't quite reach",
        action = ending_unkind_start
    ),
}


# MAKE THE GAME WORK AND UPDATES PLAYER LOCATION:

while True:
    area_place = user.location
    if area_place == "lopeta":
        save_game(user)
        quit_game_start(user)
    current_area = area_map[area_place]

    print("")
    print(f"{current_area.name}")
    print(current_area.description)
    
    next_area_place = current_area.action(user)
    user.location = next_area_place



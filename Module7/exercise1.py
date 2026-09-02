import random

def roll_dice():
    return random.randint(1, 6)

random_roll = 0
while random_roll != 6:
    random_roll = roll_dice()
    print(random_roll)
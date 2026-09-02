import random

def roll_dice(num_of_sides):
    return random.randint(1, num_of_sides)

sides = int(input("How many sides to your dice? "))


random_roll = 0
while random_roll != sides:
    random_roll = roll_dice(sides)
    print(random_roll)
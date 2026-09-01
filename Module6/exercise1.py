import random

rolls = int(input("How many dice to roll: "))

sum = 0
for roll in range(rolls):
    sum = sum + random.randint(1,6)
print(f"Sum of the dice: {sum}")
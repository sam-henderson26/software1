import random
secret_number = int(random.randint(1,10))

while True:
    guessed_number = int(input("Guess the number, between 1 and 10: "))
    if guessed_number < secret_number:
        print("Too low")
    elif guessed_number > secret_number:
        print("Too high")
    elif guessed_number == secret_number:
        print ("Correct")
        break
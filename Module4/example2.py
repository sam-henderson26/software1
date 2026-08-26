money = float(input("Give money: "))
age = float(input("Give age: "))

if money >= 3 and age >= 15:
    print("You are allowed to buy an energy drink.")
if money < 3 or age < 15:
    print("You are not allowed to buy this drink.")

# command: if, else, and elif.
# we can use the else commands for everything other than "if", and
# we can use "elif" if we want to have multiple outcomes that only read unique lines of text for each outcome
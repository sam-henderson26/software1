money = float(input("Give money: "))
age = float(input("Give age: "))

if money >= 3 and age >= 15:
    print("You are allowed to buy an energy drink.")
if money < 3 or age < 15:
    print("You are not allowed to buy this drink.")

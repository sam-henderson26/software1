

money = float(input("Give money: "))

Cost_of_coffee = 5

if money >= Cost_of_coffee:
    print("You can buy coffee")
    takeout = input("Coffee to go? ")
    if takeout == "yes":
        print("User is taking the coffee to go.")
    if takeout == "no":
        print("User is having coffee inside cafe.")

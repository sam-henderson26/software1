def get_season(month_to_season):
    if month_number == 3 or month_number == 4 or month_number == 5:
        return ("spring")
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return ("summer")
    elif month_number == 9 or month_number == 10 or month_number == 11:
        return ("autumn")
    elif month_number == 12 or month_number == 1 or month_number == 2:
        return ("winter")

month_number = int(input("Enter the number of a month (1-12): "))
season = get_season(month_number)
if month_number >= 1 and month_number <= 12:
    print(f"You entered: {month_number}")
    print(f"The season is {season}.")
else:
    print(f"You entered: {month_number}")
    print("Please enter a number between 1 and 12.")

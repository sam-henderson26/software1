list_of_airports = {}

choice = "0"

while choice != "3":
    print("")
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Please choose an option (1-3): ")

    if choice == "1":
        ICAO_code = input("Enter the ICAO code: ")
        airport_name = input("Enter the airport name: ")
        list_of_airports[ICAO_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {ICAO_code} has been added.")

    elif choice == "2":
        ICAO_code = input("Enter the ICAO code: ")
        if ICAO_code in list_of_airports:
            print(f"The airport with ICAO code {ICAO_code} is {list_of_airports[ICAO_code]}.")
        else:
            print(f"No airport found with ICAO code {ICAO_code}.")

    elif choice == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break
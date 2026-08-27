# ask user to select an option:
menu_list = "select option:\n1. add \n2. subtract \n3. multiply \n0. exit"
selection = input(menu_list)

# if the user did not select to quit
while selection != "0":
    # ask user for 2 numbers:
    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))
    # perform selected calculation:
    if selection == "1":
        print(f"Result: {first_number + second_number}")
    elif selection == "2":
        print(f"Result: {first_number - second_number}")
    elif selection == "3":
        print(f"Result: {first_number * second_number}")
    
    menu_list = "select option:\n1. add \n2. subtract \n3. multiply \n0. exit"
    selection = input(menu_list)
# with open("Module13/shopping.txt", "w") as shopping_file:
    # shopping_file.write("milk \n bread \n eggs")

# with open("Module13/shopping.txt", "a") as shopping_file:
    # shopping_file.write("\n chicken")

with open("Module13/shopping.txt", "r") as shopping_file:
    file_data = shopping_file.readlines()
    print(len(file_data))


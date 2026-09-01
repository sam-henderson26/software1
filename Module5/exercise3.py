smallest_number = None
largest_number = None

while True:
    number_list = input("Enter a number (or press Enter to quit): ")
    if number_list == "":
        break
    number = float(number_list)
    if smallest_number is None or number < smallest_number:
            smallest_number = number
    if largest_number is None or number > largest_number:
            largest_number = number

if smallest_number is not None and largest_number is not None:
    print(f"Smallest number: {smallest_number}")
    print(f"Largest number: {largest_number}")
def gallons_to_liters(gallons):
    return (gallons * 3.785)

value = float(input("Enter a volume in American gallons (negative value to quit): "))

while value >= 0:
    print(f"{value} American gallons is {gallons_to_liters(value):.2f} liters.")
    value = float(input("Enter a volume in American gallons (negative value to quit): "))
    if value < 0:
        print("Program finished.")
        break
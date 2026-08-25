talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# 1 talent = 20 pounds, 1 pound = 32 lots, 1 lot = 13.3g
# 3 9 13.5

total_pounds = ((talents * 20) + pounds)
total_lots = ((total_pounds * 32) + lots)
total_grams = total_lots * 13.3

kilograms = int(total_grams / 1000)
remaining_grams = (total_grams - (kilograms * 1000))

print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
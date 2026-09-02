import math

def calculate_unit_price(diameter, price):
    area = math.pi * ((diameter / 2 / 100) ** 2)
    return (price / area)

diameter_1 = float(input("Enter the diameter of the first pizza (cm): "))
price_1 = float(input("Enter the price of the first pizza (euros): "))

diameter_2 = float(input("Enter the diameter of the second pizza (cm): "))
price_2 = float(input("Enter the price of the second pizza (euros): "))

conversion_1 = calculate_unit_price(diameter_1, price_1)
conversion_2 = calculate_unit_price(diameter_2, price_2)

print(f"Unit price of the first pizza: {conversion_1:.2f} euros/m² Unit price of the second pizza: {conversion_2:.2f} euros/m²")

if conversion_1 > conversion_2:
    print("The second pizza provides better value for money.")
elif conversion_1 < conversion_2:
    print("The first pizza provides better value for money.")
else:
    print("Both of the pizzas are equal in cost/size.")
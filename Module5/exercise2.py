# Write a program that converts inches to centimeters
# until the user inputs a negative value. Then the program ends.

inches = float(input("Enter length in inches (negative value to quit): "))
if inches < 0:
        print ("Program ended.")

while inches >= 0:
    centimeters = (inches * 2.54)
    print (f"{inches} inches is {centimeters:.2f} centimeters")
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        print ("Program ended.")


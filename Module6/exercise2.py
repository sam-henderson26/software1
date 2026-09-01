number = input("Enter a number: ")

numbers = []

while number != "":
    numbers.append(float(number))
    number = input("Enter a number: ")

numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for n in numbers[:5]:
    print(n)

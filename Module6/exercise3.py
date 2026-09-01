number = int(input("Enter an integer: "))

if number <= 1:
    print(number, "is not a prime number.")
else:
    potential_prime = True
    for i in range(2, number):
        if number % i == 0:
            potential_prime = False
            break
    if potential_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
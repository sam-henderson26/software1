# Sometimes there is a need to store some information that applies to the entire class.
# For example the total amount of objects (dogs) in the class.
# underneath example, a class variable called "created" is made to store the number of dogs.

class Dog:
    created = 0

    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created = Dog.created + 1

dog1 = Dog("Head", 2018)
dog2 = Dog("Shoulders", 2022, "Yip yip yip")
print(f"{Dog.created} dogs have been created so far.")

# value of a class variable is made by putting the class (Dog) with the variable (created),
# combined with a full stop. (Dog.created)

# Class, object, initializer:

# a class is a general concept that determines
# common and shared properties for the members of the class.

class Dog:
    pass

# the pass statement is an empty placeholder, just to help show the class "Dog".

# Here is how we create a Dog object called Bubbles that was born in 2022:

dog = Dog()
dog.name = "Bubbles"
dog.birth_year = 2022

print(f"{dog.name:s} was born in {dog.birth_year:d}." )

# This way of adding objectss to a class takes a long time,
# we can use initialisers to speed things up.

class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

dog = Dog("Bubbles", 2022)

print(f"{dog.name:s} was born in {dog.birth_year:d}." )

# Methods:
# Let’s write a bark method to our Dog class.

class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return


dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

print(f"{dog1.name:s} was born in {dog1.birth_year:d}." )
dog1.bark(2)
print(f"{dog2.name:s} was born in {dog2.birth_year:d}." )
dog2.bark(5)

# Now the association has 3 parameters, the bark parameter has been given a default
# sound as "Woof woof", so if a sound is not given, the object will use this default
# sound.
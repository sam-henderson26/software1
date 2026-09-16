# Associations:
# last example from module 9:

class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

# If we add another class, such as a dog hotel:

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

# Main program

dog1 = Dog("sam", 2018)
dog2 = Dog("maia", 2022, "Yip yip yip")

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

hotel.dog_checkout(dog1)
hotel.greet_dogs()

# This example consists of 3 parts: dog class, hotel class, and the main program.
# The execution begins with 2 dogs being created, then a hotel.
# Then the initialiser of the hotel class begins, where an empty dogs list is created,
# Then the first dog is added to the list. 



#class Dog:
#    def __init__(self, name, year_of_birth, bark="woof"):
#        self.name = name
#        self.year_of_birth = year_of_birth
#        self.bark = bark
#    def bark(self, times):
#        for i in range(times):
#            print(f"{self.name} barks {self.bark}")

#class Hotel:
#    def __init__(self):
#        self.dogs = []
#    def dog_checkin(self, dog):
#        self.dogs.append(dog)
#    def dog_checkout(self, dog):
#        self.dogs.remove(dog)
#    def greet_dogs(self):
#        for dog in self.dogs:
#            dog.bark(1)
#dog1 = Dog("Sam", 2020)
#dog2 = Dog("Maia", 2019)
#hotel = Hotel()

#hotel.dog_checkin(dog1)
#hotel.dog_checkin(dog2)
#hotel.greet_dogs()
#hotel.dog_checkout(dog2)
#hotel.greet_dogs()
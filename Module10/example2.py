# Temporary associations:
# lets use an example of a car going to be repainted:

class Car:
    def __init__(self, plate_number, colour):
        self.plate_number = plate_number
        self.colour = colour

class PaintShop:
    def paint(self, car, colour):
        car.colour = colour

paint_shop = PaintShop()
car = Car("ABC-123", "blue")
print("The car is " + car.colour)
paint_shop.paint(car, "red")
print("The car is now " + car.colour)

# In this example, the paint shop knows the car only for the execution of the "paint" method.
# This is because the "Car" object was received as a parameter of the method call.
# When the execution of the method is finished, the value of the vraiable can no longer be accessed.
# The Car (object) also has no knowledge of the paint shop.
# associative relationship between the paint shop and the car is only temporary.

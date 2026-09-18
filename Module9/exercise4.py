import random

class Car:
    def __init__(self, license_plate, maximum_speed, current_speed = 0, travelled_distance =2000, ):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, time):
        self.travelled_distance += self.current_speed * time

car1 = Car("ABC-123", 142)
car2 = Car("DEF-456", 142)
car3 = Car("GHI-789", 142)

car1.accelerate
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
        

# From exercise 2 ^^ + drive method.

car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")

# answer is correct on moodle when removinig the 2 print commands (23 and 26).
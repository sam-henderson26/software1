class Car:
    def __init__(self, license_plate, maximum_speed, current_speed = 0, travelled_distance =0 ):
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

car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Current speed: {car1.current_speed} km/h")
car1.accelerate(-200)
print(f"Current speed: {car1.current_speed} km/h")
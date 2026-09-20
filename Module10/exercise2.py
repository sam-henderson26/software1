class Elevator:
    def __init__ (self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up (self):
        if self.current_floor < self.top_floor:
            self.current_floor +=1
            print(f"elevator going up, now at {self.current_floor}")

    def floor_down (self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -=1
            print(f"elevator going down, now at {self.current_floor}")

    def go_to_floor (self, chosen_floor):
        while self.current_floor < chosen_floor:
            self.floor_up()
        while self.current_floor > chosen_floor:
            self.floor_down()


class Building:
    def __init__ (self, bottom_floor, top_floor, number_of_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor

        self.elevators = []
        for n in range(number_of_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, chosen_floor):
        selected_elevator = self.elevators[elevator_number]
        selected_elevator.go_to_floor(chosen_floor)

# Test Building with multiple elevators
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 3)
building.run_elevator(2, 8)

# Test single elevator building
small_building = Building(0, 5, 1)
small_building.run_elevator(0, 4)

# Test larger building
office = Building(1, 6, 5)
office.run_elevator(0, 4)
office.run_elevator(4, 2)
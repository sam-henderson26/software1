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

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
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

# Your test code
h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)
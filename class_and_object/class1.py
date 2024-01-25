class Vehicle:
    COLOR = "Red"

    def __init__(self, color) -> None: # constructor
        print("called")
        self.COLOR = color
    
    def get_color(self):
        self.COLOR


truck = Vehicle()
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying. ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing. 🛥️")

# Create a list of different vehicle objects
vehicles = [
    Car("Sedan"),
    Plane("Boeing 747"),
    Boat("Sailboat"),
    Car("Sports Car")
]

# Iterate through the list and call the move() method on each object
for vehicle in vehicles:
    vehicle.move()
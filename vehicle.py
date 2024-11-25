# vehicle.py

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")

class Bike(Vehicle):
    def move(self):
        print("The bike rides on the road.")

class Plane(Vehicle):
    def move(self):
        print("The plane flies in the sky.")

# Demonstrating polymorphism
def demonstrate_move(vehicle: Vehicle):
    vehicle.move()

# Example usage
car = Car()
bike = Bike()
plane = Plane()

demonstrate_move(car)   # Output: The car drives on the road.
demonstrate_move(bike)  # Output: The bike rides on the road.
demonstrate_move(plane) # Output: The plane flies in the sky.

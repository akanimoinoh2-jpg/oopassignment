# Class Variable
class Car:
    wheels = 4  # Class variable (shared by all cars)

    def __init__(self, make, model, year):
        # Object Variables (instance variables)
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed = max(0, self.speed - 10)

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Speed: {self.speed} km/h")
        print(f"Wheels: {Car.wheels}")
        


# Creating two Car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Demonstrating behavior for car1
car1.accelerate()
car1.brake()
car1.display_info()

# Demonstrating behavior for car2
car2.accelerate()
car2.display_info()
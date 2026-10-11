# Class car and its methods
class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    def print_brand(self):
        print("Brand:", self.brand)

    def print_colour(self):
        print("Colour:", self.colour)

car1 = Car("Toyota", "Red")
car1.print_brand()
car1.print_colour()

class Vehicle:
    
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def print_car(self):
        print("This vehicle is a {} {} {} in {}".format(self.year, self.make, self.model, self.color))

    
car = Vehicle("DMC", "Delorean", 1983, "Grey")
car.print_car()


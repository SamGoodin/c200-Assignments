class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.acc = []

    def addAccessory(self, a):
        self.acc.append(a)

    def __repr__(self):
        return "(Car: " + str(self.year) + ", " + self.make + ", " + self.model + ")"


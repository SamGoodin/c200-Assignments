class Car:
    """
    Class to represent the make, model, and year of a car
    """

    def __init__(self, theMake, theModel, theYear):
        """
        Takes in a string for the make, the model, and int representing the year
        """
        self.make = theMake
        self.model = theModel
        self.year = theYear

    def getMake(self):
        #Returns make of the car
        return self.make

    def getModel(self):
        #Returns the model of the car
        return self.model

    def getYear(self):
        #Returns the year of the car
        return self.year

    def setYear(self, year):
        #Given a year, update the year of the car
        self.year = year

    def olderCar(self, otherCar):
        #Given a different car, return the instance of the older car
        if self.year < otherCar.year:
            return self
        else:
            return otherCar

    def stringRep(self):
        #Returns the string representation of the car class
        return "Make: {0}\nModel: {1}\nYear: {2}\n".format(self.make, self.model, self.year)
    
    def __repr__(self):
        return self.stringRep()

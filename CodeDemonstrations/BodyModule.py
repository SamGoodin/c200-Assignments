from CarClass import Car 
#from <module> import <class>

class Sedan(Car):
    #Sedan class that inherits from the car class

    def __init__(self, mk, mdl, yr):
        Car.__init__(self, mk, mdl, yr)
        self.doorCount = 4

    def getDoorCount(self):
        return self.doorCount

    def __repr__(self):
        return self.stringRep() + "Door Count: {0}\n".format(self.getDoorCount())

class Minivan(Car):

    def __init__(self, mk, mdl, yr):
        Car.__init__(self, mk, mdl, yr)
        self.doorCount = 4

    def getDoorCount(self):
        return self.doorCount

    def __repr__(self):
        return self.stringRep() + "Door Count: {0}\n".format(self.getDoorCount())

class Truck(Car):

    def __init__(self, mk, mdl, yr, doorCount):
        Car.__init__(self, mk, mdl, yr)
        self.doorCount = doorCount

    def getDoorCount(self):
        return self.doorCount

    def __repr__(self):
        return self.stringRep() + "Door Count: {0}\n".format(self.getDoorCount())
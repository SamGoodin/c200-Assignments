class Coffee:

    def __init__(self, drink, roast, price, quantity):
        self.drink = drink
        self.roast = roast
        self.price = price
        self.quantity = quantity

    def getDrink(self):
        return self.drink

    def getRoast(self):
        return self.roast

    def getPrice(self):
        s = str(self.price).split(".")
        if len(s[-1]) == 1:
            st = "{0}.{1}0".format(s[0], s[1])
            return st
        else:
            return self.price

    def getQuantity(self):
        return self.quantity

    def inStock(self):
        if not (self.quantity == 0):
            return True
        else:
            return False

    def sold(self):
        self.quantity -= 1
        return float(self.getPrice())

    def toString(self):
        st = "A {0} roast {1} costs ${2} and ".format(self.roast, self.drink, self.getPrice())
        if self.inStock():
            st += "is in stock."
        else:
            st += "is not in stock."
        return st
        #return "Drink: {0}\nRoast: {1}\nPrice: {2}\nQuantity: {3}".format(self.drink, self.roast, str(self.price), str(self.quantity))

    def __repr__(self):
        return self.toString()

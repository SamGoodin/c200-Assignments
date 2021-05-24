class Book:

    def __init__(self, title, firstName, lastName, price, quantity):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.price = price
        self.quantity = quantity

    def getTitle(self):
        return self.title
    
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

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
        if not (self.getQuantity() == 0):
            return True
        else:
            return False

    def sold(self):
        self.quantity -= 1
        return float(self.getPrice())

    def toString(self):
        st = "{0} by {1} {2} costs ${3} and ".format(self.title, self.firstName, self.lastName, self.getPrice())
        if self.inStock():
            st += "is in stock."
        else:
            st += "is not in stock."
        return st
        #return "Title: {0}\nAuthor: {1} {2}\nPrice: {3}\nQuantity: {4}\n".format(self.title, self.firstName, self.lastName, str(self.price), str(self.quantity))

    def __repr__(self):
        return self.toString() 

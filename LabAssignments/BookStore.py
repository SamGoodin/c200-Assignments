class BookStore:

    def __init__(self, bookList, coffeeShop):
        self.bookList = bookList
        self.coffeeShop = coffeeShop

    def bookSearch(self, title):
        for book in self.bookList:
            if book.getTitle() == title:
                return book

    def authorSearch(self, firstName, lastName):
        for book in self.bookList:
            if book.getFirstName() == firstName and book.getLastName() == lastName:
                return book

    def coffeeSearch(self, drink, roast):
        for coffee in self.coffeeShop.coffeeList:
            if coffee.drink == drink and coffee.roast == roast:
                return coffee

    def sale(self, bookSold=None, coffeeSold=None):
        totalAmount = 0
        if bookSold:
            for book in bookSold:
                totalAmount += self.bookSearch(book).sold()
        if coffeeSold:
            for coffee in coffeeSold:
                sp = coffee.split(" ")
                totalAmount += self.coffeeSearch(sp[0], sp[1]).sold()
        return totalAmount


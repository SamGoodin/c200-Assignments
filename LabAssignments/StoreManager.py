from BookStore import BookStore
from Book import Book
from CoffeeShop import CoffeeShop
from Coffee import Coffee


# we will store our book objects in a list
bookList = []
bookList.append(Book("Brave New World", "Aldous", "Huxley", 12.75, 2))
bookList.append(Book("Jane Eyre", "Charlotte", "Bronte", 10.50, 4))
bookList.append(Book("Pride and Prejudice", "Jane", "Austen", 15.00, 1))
bookList.append(Book("In Search of Lost Time", "Marcel", "Proust", 9, 0))
bookList.append(Book("Wuthering Heights", "Emily", "Bronte", 10.50, 3))
bookList.append(Book("Rebecca", "Daphne", "du Maurier", 9, 2))

# we store our coffee objects in a list
coffeeList = []
coffeeList.append(Coffee("Coffee", "Dark", 3.50, 10))
coffeeList.append(Coffee("Coffee", "Medium", 3.00, 5))
coffeeList.append(Coffee("Coffee", "Light", 4.00, 7))
coffeeList.append(Coffee("Espresso", "Medium", 4.50, 5))
coffeeList.append(Coffee("Latte", "Light", 5.50, 5))
coffeeList.append(Coffee("Mocha", "Medium", 5.25, 3))

# create a new coffee shop to pair with this book store
coffeeshop = CoffeeShop(coffeeList)

# create the book store
bookStore = BookStore(bookList, coffeeshop)



##### Make some sales! #####
print(bookStore.bookSearch("Brave New World").toString())
print(bookStore.coffeeSearch("Coffee", "Dark").toString())
print("\n\n")
print(bookStore.bookSearch("Brave New World").getQuantity())
print(bookStore.coffeeSearch("Coffee", "Dark").getQuantity())
print("\n\n")
amountDue = bookStore.sale(["Brave New World"], ["Coffee Dark"])
print("You owe ${0:.2f} for your purchases today.".format(amountDue))
print("\n\n")
print(bookStore.bookSearch("Brave New World").getQuantity())
print(bookStore.coffeeSearch("Coffee", "Dark").getQuantity())

def enterSell(cob):
    pass

def enterBuy(cob):
    if cob == "books":
        print(bookStore.bookList)
        choice = input("Which book would you like to buy? (title) ")
        bookStore.sale(choice)
    else:
        print(coffeeshop.coffeeList)
        choice = input("What coffee would you like to buy? (drink roast) ").split(" ")

flag = True
while flag:
    buyOrSell = input("Are you looking to buy or sell? (q == quit) ")
    if buyOrSell.lower() == "buy":
        s = input("What would you like to buy? (coffee or books) ")
        enterBuy(s)
    elif buyOrSell.lower() == "sell":
        s = input("What would you like to sell? (coffee or books) ")
    elif buyOrSell.lower() == "q":
        flag = False

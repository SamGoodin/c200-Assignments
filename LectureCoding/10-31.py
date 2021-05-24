class Account:
    ID = 1
    
    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    def withdraw(self, amount):
        if amount > self.balance:
            return 0
        else:
            self.balance -= amount
            return amount

    def deposit(self, amount):
        self.balance += amount
        return self

    def current_balance(self):
        return self.balance

    def __str__(self):
        return str(self.balance)

class Bank(Account):

    def __init__(self, name, initial_deposit):
        self.name = name
        Account.__init__(self, initial_deposit)
        self.ID = Account.ID
        Account.ID += 1

    def get_ID(self):
        return self.ID

    def __str__(self):
        return "Name: {0}\nID: {1}\nBalance: {2}\n".format(self.name, self.get_ID(), self.current_balance())

    def get_my_account(self):
        inputID = int(input("Enter ID: "))
        if not (inputID == self.ID):
            print("No...not gonna happen")

g = Account(500)
g.deposit(200).deposit(50).deposit(87)
print(g.withdraw(50))
print(g.current_balance())
print(g)

x1 = Bank("Kaiser", 100)
print(x1)
x2 = Bank("Ursala", 200)
print(x2)
x3 = Bank("Shilah", 75)
print(x3)

x2.deposit(x1.withdraw(50)).withdraw(100)
print(x1)
print(x2)

x1.get_my_account()

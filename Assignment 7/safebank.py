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
        #ignore this method -- you can use it, but assume nobody can access it.
        return self.balance

class Bank(Account):

    def __init__(self, name, initial_deposit):
        self.name = name
        Account.__init__(self, initial_deposit)
        self.ID = Account.ID
        Account.ID += 1
        self.locked_out = False

    def __str__(self):
        return "Name: {0} ID: {1} Balance: {2}".format(self.name, self.ID, self.current_balance())

    def call(self):
        self.locked_out = False

    def withdraw(self, amount):
        if self.securityCheck():
            return super().withdraw(amount)
        else:
            return "This account is locked. Please call to unlock."

    def deposit(self, amount):
        if self.securityCheck():
            return super().deposit(amount)
        else:
            return "This account is locked. Please call to unlock."

    def get_balance(self):
        if self.securityCheck():
            return self.balance
        else:
            return "This account is locked. Please call to unlock."

    def securityCheck(self):
        if self.locked_out:
            return False
        else:
            count = 0
            while count != 3:
                id = int(input("What is the ID for account name: " + self.name + " "))
                if id == self.ID:
                    return True
                else:
                    count += 1
            else:
                self.locked_out = True
                return False

x1 = Bank("Kaiser", 100)
x2 = Bank("Ursula", 200)
x3 = Bank("Shilah", 75)

print(x1.get_balance())
print(x1.withdraw(20))
print(x1.deposit(20))



#Sam Goodin 9/8/17

def addition(x, y):
    return x + y

def subtraction(x, y):
    #Subtracts variable y from x
    return x - y

def multiplication(x, y):
    #Multiplies variables x & y
    return x * y

def division(x, y):
    #Divides variable y from x
    return x / y

def max(x, y):
    if x >= y:
        return x
    else:
        return y

def min(x, y):
    if x <= y:
        return x
    else:
        return y

def welcome(name):
    #This function prints a welcome message
    print("Welcome", name)

a = addition(1, 3)
s = subtraction(10, 5)
m = multiplication(40, 20)
d = division(4, 2)
maximum = max(5, 4)
minimum = min(5, 4)
welcome(input("Who are you? "))

print("Math: ", a, s, m, d, maximum, minimum)
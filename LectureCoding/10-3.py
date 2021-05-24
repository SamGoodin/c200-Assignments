'''
#If not assigned in parameter, checks global memory for var j
def fun(i):
    print(j)

j = 50
fun(40)
'''
'''
def f(x):
    x += 1
    return x

def g(x, y):
    return x + y

def h(i):
    return 2 + i

x = 10
y = 1
x = g(x, f(y))
print(x)
print(y)
#Result: 12, 1
'''
'''
def f(x):
    x += 1
    return x

def g(x, y):
    return x + y

def h(i):
    return 2 + i

x = 10
y = h(1)
x = g(x, h(f(y)))
print(x)
print(y)
#Result: 16, 3
'''
'''
def hee(x):
    if x >= 3:
        return x * 2
    else:
        return x + hee(x-1)

def haw(x):
    if x <= 0:
        return 1
    else:
        return x * haw(x - 2)

x = hee(haw(4))
print(x)
#Result: 16
'''
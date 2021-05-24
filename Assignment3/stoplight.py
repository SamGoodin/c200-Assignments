import math

def y(d, r, t):
    return (d*math.exp((r * t)))

def N(n, m, t):
    return (n * math.exp(m * t))

def rate(age):
    if age >= 18:
        return 4
    elif 6 <= age <= 10:
        return 2
    elif 11 <= age <= 15:
        return 2.5
    elif 16 <= age < 18:
        return 3

def DWtime(w, r):
    return ((w / r) - 6)

print(y(1000, .02, 10))
print(N(500, 100, 4))
print(DWtime(30, rate(7)))

def f():
    k = 1 + 1

g = f()
print(g)
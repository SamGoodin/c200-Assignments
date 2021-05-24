'''
a(1) = 3
a(n) = 2 x a(n-1) + 5
a(3) = 2 x a(2) + 5 = 2 x (2 x a(1) + 5) + 5 = 2 x (2 x 3 + 5) + 5
'''
def aForLoop(n):
    sum = 3
    for i in range(1, n):
        sum = sum * 2 + 5
    return sum
            

def aWhileLoop(n):
    sum = 3
    while n > 1:
        sum = sum * 2 + 5
        n -= 1
    return sum

def aRecursive(n):
    if n is 1:
        return 3
    else:
        return 2 * aRecursive(n-1) + 5


'''
h(0) = 0
h(1) = 3
h(n) = h(n-1) + 2 x h(n-2), for n >= 2
h(3) = h(2) + 2 x h(1) = (h(1) + 2 x h(0)) + 2 x 3 = (3 + 2 x 0) + 2 x 3
'''

def hForLoop(n):
    sum = 0
    l = []
    for i in range(2, n+1):
        if i is 2:
            sum = (3 + 2 * 0)
        elif i is 3:
            sum = (l[0] + 2 * 3)
        else:
            sum = (l[i-3] + 2 * l[i-4])
        l.append(sum)
    return sum

def hWhileLoop(n):
    sum = 0
    l = []
    counter = 2
    while counter < (n+1):
        if counter is 2:
            sum = (3 + 2 * 0)
        elif counter is 3:
            sum = (l[0] + 2 * 3)
        else:
            sum = (l[counter-3] + 2 * l[counter-4])
        l.append(sum)
        counter += 1
    return sum

def hRecursive(n):
    if n is 0:
        return 0
    elif n is 1:
        return 3
    else:
        return hRecursive(n-1) + 2 * hRecursive(n-2)

'''
e(0) = 1
e(n) = 2 x e(n-1) + 2
e(2) = 2 x e(1) + 2 = 2 x (2 x e(0) + 2) + 2 = 2 x (2 x 1 + 2) + 2
'''

def eForLoop(n):
    sum = 1
    for i in range(0, n):
        sum = sum * 2 + 2
    return sum

def eWhileLoop(n):
    sum = 1
    while n > 0:
        sum = sum * 2 + 2
        n -= 1
    return sum

def eRecursive(n):
    if n is 0:
        return 1
    else:
        return 2 * eRecursive(n-1) + 2

print(aForLoop(2))
print(aWhileLoop(2))
print(aRecursive(2))
print(hForLoop(2))
print(hWhileLoop(2))
print(hRecursive(2))
print(eForLoop(2))
print(eWhileLoop(2))
print(eRecursive(2))
print()
print(aForLoop(3))
print(aWhileLoop(3))
print(aRecursive(3))
print(hForLoop(3))
print(hWhileLoop(3))
print(hRecursive(3))
print(eForLoop(3))
print(eWhileLoop(3))
print(eRecursive(3))
print()
print(aForLoop(4))
print(aWhileLoop(4))
print(aRecursive(4))
print(hForLoop(4))
print(hWhileLoop(4))
print(hRecursive(4))
print(eForLoop(4))
print(eWhileLoop(4))
print(eRecursive(4))
print()
print(aForLoop(6))
print(aWhileLoop(6))
print(aRecursive(6))
print(hForLoop(6))
print(hWhileLoop(6))
print(hRecursive(6))
print(eForLoop(6))
print(eWhileLoop(6))
print(eRecursive(6))
print()
print(aForLoop(26))
print(aWhileLoop(26))
print(aRecursive(26))
print(hForLoop(26))
print(hWhileLoop(26))
print(hRecursive(26))
print(eForLoop(26))
print(eWhileLoop(26))
print(eRecursive(26))
f = lambda x: x if (x % 2 == 0) else x + 1
g = lambda x, y: x * y
aa = [1, 2, 3, 4]
bb = [3, 1, 4, 2]

x = [f(x) for x in range(6)]
y = [i for i in range(1, 10, 2) if i > 3]
z = list(map(g, aa, bb))

some_numbers = range(2, 100)

for i in range(2, 20):
    some_numbers = list(filter(lambda x: x == i or x % i, some_numbers))

print(x)
print(y)
print(z)
print(some_numbers)

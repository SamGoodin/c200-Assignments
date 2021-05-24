#NUMBER 1
'''
[0] + 0
Answer: ERROR
'''
print([] + ['a', 2]) 
#Answer: ['a', 2]
print([] + [1, 3] + ['b']) 
#Answer: [1, 3, 'b']
print('hello' + 2*'kitty')
#Answer: 'hellokittykitty'
print([1, 3, 4] + ['a'])
#Answer: [1, 3, 4, 'a']
'''
[1, 3, 4] - [1, 3]
Answer: ERROR (can't subtract lists)
'''
print(',' + 'Rick a' + 'nd' + 'Morty')
#Answer: ',Rick andMorty'
print(3 * [] + 3 * [3])
#Answer: [3, 3, 3]

#NUMBER 2
#Both are turing complete languages, can do the
#same things.

#NUMBER 3
#State, choice, and loop.

#NUMBER 4
x = range(2, 22, 5) #creates list [2, 7, 12, 17]
q = []
for i in range(0, len(x)):
    q = q + [x[i]]
print(q)
#Answer: [2, 7, 12, 17]

#NUMBER 5
#While loop
l = []
step = 3
num = 0
while(num < 100):
    l.append(num)
    num += step
    step += 2
print(l)
#For loop
l = []
step = 3
num = 0
for n in range(100):
    l.append(num)
    if (num + step <= 99):
        num += step
        step += 2
    else:
        break
print(l)

#NUMBER 6
#Returns how many times int x is in list y
#Answer: 2
#Answer: 0

#NUMBER 7
#Compares every int at index i with both lists,
#adds bigger num to m, returns m.
#Answer: [2, 4, 4, 5]

#NUMBER 8
#For loop
def rf(x):
    l = []
    for i in x:
        if not (i%2 == 0):
            l.append(i)
    return l

#While loop
def rw(x):
    l = []
    num = 0
    while num < len(x):
        if not (x[num] % 2 == 0):
            l.append(x[num])
        num += 1
    return l

#Recursion
def rr(x):
    if x == []:
        return []
    else:
        if x[0]%2 == 0:
            return rr(x[1:])
        else:
            return [x[0]] + rr(x[1:])

print(rf([1, 2, 3, 4, 5]))
print(rw([1, 2, 3, 4, 5]))
print(rr([1, 2, 3, 4, 5]))

#NUMBER 9
def s(x):
    sum = 0
    if x is []:
        return sum
    else:
        for i in x:
            sum += i
        return sum

print(s([1, 4, 5, -2]))

#NUMBER 10
def ss(x):
    if x is []:
        return 0
    else:
        l = []
        for i in x:
            sum = 0
            for j in i:
                sum += j
            l.append(sum)
        return l

print(ss(([1, 2, 3], [], [4, -4, 4])))

#NUMBER 11

#NUMBER 12
x = 0
for i in range(1, 4):
    x = x + i ** 2
print(x)
#Same thing
x = 0
i = 1
x = x + i ** 2

i = 2
x = x + i ** 2

i = 3
x = x + i ** 2

print(x)

#NUMBER 13
a = 10
while a > 1:
    a = a -4
    print(2*a)
#Same thing
a = 10
if a > 1:
    a -= 4
    print(2*a)

if a > 1:
    a -= 4
    print(2*a)

if a > 1:
    a -= 4
    print(2*a)

#NUMBER 14
#Answer: 8

#EXTRA CREDIT
def m(s):
    if s:
        return s[0] == s[-1] and m(s[1: -1])
    else:
        return True

x = ["kitty", "amanaplanpanama", "atoyota", "ratsliveonnoevilstar"]

for i in x:
    print(m(i))
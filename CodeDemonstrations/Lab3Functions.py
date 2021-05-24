"""
Sam Goodin 9/8/17
In-lab Assignment 3
"""

def maxThree(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > y and z > x:
        return z

def minThree(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < y and z < x:
        return z

def maxTwoSum(x, y, z):
    sum = 0
    if x > y or x > z:
        sum += x
    if y > x or y > z:
        sum += y
    if z > x or z > y:
        sum += z
    return sum

def minTwoSum(x, y, z):
    sum = 0
    if x < y or x < z:
        sum += x
    if y < x or y < z:
        sum += y
    if z < x or z < y:
        sum += z
    return sum

def maxList(l):
    bigNum = l[0]
    for i in l:
        if i > bigNum:
            bigNum = i
    return bigNum

def minList(l):
    lilNum = l[0]
    for i in l:
        if i < lilNum:
            lilNum = i
    return lilNum

print(maxThree(10, 2, 32))
print(minThree(10, 2, 32))
print(maxTwoSum(10, 2, 32))
print(minTwoSum(10, 2, 32))
print(maxList([10, 27, 3, 14, 5]))
print(minList([10, 27, 3, 14, 5]))

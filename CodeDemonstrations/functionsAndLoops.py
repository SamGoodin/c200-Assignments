#Sam Goodin 9/15/17

#Sums all numbers in a list using a for-loop
def sumListFor(aList):
    result = 0
    for number in aList:
        result += number
    return result

aL = [1, 2, 3, 4]

result = sumListFor(aL)

print("Adding list: " + str(result))

# Multiply the numbers in a list together using a while-loop
def multiplyListWhile(aList):
    result = 0
    counter = 0
    listLen = len(aList)
    while counter < listLen:
        result *= aList[counter]
        counter += 1
    return result

multList = multiplyListWhile(aL)

print("Multiply List: " + str(multList))

def factorialForLoop(n):
    result = 1
    for number in range(1, n+1):
        result *= number
    return result

fact = factorialForLoop(5)
print("Factorial of 5: " + str(fact))
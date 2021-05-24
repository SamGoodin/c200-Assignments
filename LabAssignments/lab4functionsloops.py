# Sam Goodin 9/15/17
# Lab Assignment Week 4
# To be checked-off
# The use of min, max, sum, map, etc. functions that would be deemed shortcuts is prohibited 
#
# Please call the function at the bottom of the code and print the result.
# None of the functions should call PRINT
# 
# Created by Larry Gates
# Please commit to the repository

# Question 1
# Sums all the numbers in a list using a while-loop
def sumListWhile(aList):
    result = 0
    counter = 0
    while counter < len(aList):
        result += aList[counter]
        counter += 1
    return result


# Question 2
# Multiply the numbers in a list together using a for-loop
def multiplyListFor(aList):
    result = 1
    for i in aList:
        result *= i
    return result


# Question 3
# Return the factorial of n using a while-loop
def factorialWhileLoop(n):
    result = 1
    counter = 1
    while counter < n+1:
        result *= counter
        counter += 1
    return result



# Question 4 (Challenge Problem (Bonus))
# TODO: Write functions that perform the multiplication and division using for and while loops

# Part a: For loop - Multiplication
# Write a function taking in 2 arguments. Then use a for loop to multiply the numbers together. 

# TODO: Write function

def forMultiplication(*args):
    l = []
    for a in args:
        l.append(a)
    result = 1
    for i in l:
        result *= i
    return result


# Part b: For loop - Division
# Write a function taking in 2 arguments. Then use a for loop to divide the numbers. 

# TODO: Write function

def forDivision(*args):
    l = []
    for a in args:
        l.append(a)
    result = l[0]
    for i in l:
        num = l.index(i)
        result /= l[num+1]
        if num + 1 == len(l):
            break
        else:
            pass
    return result


# Part c: While loop - Multiplication
# Write a function taking in 2 arguments. Then use a while loop to multiply the numbers together. 

# TODO: Write function

def whileMultiplication(*args):
    l = []
    for a in args:
        l.append(a)
    result = 1
    counter = 0
    while counter < len(l):
        result *= l[counter]
        counter += 1
    return result

# Part d: While loop - Division
# Write a function taking in 2 arguments. Then use a while loop to divide the numbers. 

# TODO: Write function

def whileDivision(num1, num2):
    pass


################ Print the Result of calling each of the functions ################
print(sumListWhile([1, 2, 3, 4]))
print(sumListWhile([5, 10, 15, 20]))
print(multiplyListFor([1, 2, 3, 4]))
print(multiplyListFor([5, 10, 15, 20]))
print(factorialWhileLoop(5))
print(factorialWhileLoop(10))
print(forMultiplication(2, 3))
print(forDivision(2, 3))
print(whileMultiplication(2, 3))
print(whileDivision(2, 3))
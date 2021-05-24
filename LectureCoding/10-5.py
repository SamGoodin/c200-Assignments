'''
h(5) = 2 * 5 + h(4)
h(4) = 2 * 4 + h(3)
h(3) = 2 * 3 + h(2)
h(2) = 2 * 2 + h(1)
h(1) = 2 * 1 + h(0)
h(0) = 2

h(5) = 2 * 5 + (2 * 4 + (2 * 3 + (2 * 2 + (2 * 1 + 2))))
h(5) = 32
'''
'''
def h(n):
    if n is 0:
        return 2
    else:
        return 2 * n + h(n-1)

def h1(n):
    i = 2
    for j in range(1, n+1):
        i += j*2
    return i

print(h(5))
print(h1(5))
'''

import random

x = random.randrange(0, 11)
guess = 3
number = int(input("Guess a number between 0 and 10: "))

while not (number == x) and not (guess == 1):
    guess -= 1
    print("You can do it! We're in this together :)")
    print("You only have {0} guesses left ><.".format(guess))
    if number > x and number < 11:
        print("Guess a lower number.")
    elif number < x and number > -1:
        print("Guess a higher number.")
    number = int(input("Guess a number between 0 and 10: "))


#player who guesses number
#computer that says whether the secret number is correct

#get user input of the secret number
#computer pick a secret number
#types of number 0 to 10

#while user hasn't guessed the number
#   get user to guess again

#message about current winning or losing
#play multiple times

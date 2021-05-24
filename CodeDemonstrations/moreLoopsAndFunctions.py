#Sam Goodin 9/22/17
import math

nameList = ["Max", "Maddy", "Aiyun", "EJ", "Joshua", "Kurt", "Larry", "Sahiti", "Ishita"]

def middleCharacter(string):
    strLen = len(string)
    middleOfString = math.floor(strLen/2)
    return string[middleOfString]

def getMiddleCharacterList(aList):
    string = ""
    for i in range(0, len(aList)):
        currentString = aList[i]
        middleChar = middleCharacter(currentString)
        string += middleChar
    return string

def getLetterCount(givenString, character):
    counter = 0
    totalCount = 0
    while counter < len(givenString):
        ch = givenString[counter]
        if ch is character:
            totalCount += 1
        counter += 1
    return totalCount

result = getMiddleCharacterList(nameList)
print(result)

ch = "a"
st = "supercalifragilisticexplialidocious"

counter = getLetterCount(st, ch)
print("The character " + ch + " appears in " + st + " " + str(counter) + " time(s).")
# Samuel Goodin 10/20/17

# Given a file with animals and current population, print out
# the animals that are less than the default threshold.

# Task: Create a dictionary(animal, population)
# Task: Open the file in read mode
# Task: Read the file for the data
# Task: Parse the file contents into a structure

def readFile(fileLocation):
    # Reads the file and returns a list of all lines
    rawData = []
    with open(fileLocation, 'r') as file:
        for line in file:
            rawData.append(line.strip())
    return rawData

def parseFile(data):
    # Returns a dictionary with animal as key and population as value
    speciesDict = {}
    for species in data:
        dataStrings = species.split(":")
        animal = dataStrings[0]
        population = int(dataStrings[1])
        speciesDict[animal] = population
    return speciesDict

def computationStep(speciesDict):
    # For each species in the dictionary, determine if the animal is endangered
    endangeredList = []
    for species in speciesDict:
        if speciesDict[species] < 5000:
            endangeredList.append(species)
    return endangeredList

def display(result):
    print(result)

def main():
    data = readFile("SpeciesData.txt")
    dictionary = parseFile(data)
    finalResult = computationStep(dictionary)
    display(finalResult)

main()
ar = ["o", "as", "a", "amos", "ais", "an"]
er = ["o", "es", "e", "emos", "eis", "en"]
ir = ["o", "es", "e", "imos", "is", "en"]

endings = {
    "ar": ar,
    "er": er,
    "ir": ir
}

conversion = {
    "i": [0, "Yo"],
    "you": [1, "Tu"],
    "he": [2, "El"],
    "she": [2, "Ella"],
    "it": [2, "Usted"],
    "we": [3, "Nosotros"],
    "they all": [4, "Vosotros"],
    "they": [5, "Ustedes"]
    }

words = [["to buy", "comprar"], ["to speak", "hablar"], ["to learn", "apprender"], ["to receive", "recibir"]]

def getVerb(v):
    mainCounter = 0
    while mainCounter < len(words):
        if v in words[mainCounter][0]:
            return words[mainCounter][1]
        mainCounter += 1

def getEnding(v):
    return v[-2:]

def conjugate(v):
    verb = getVerb(v)
    if verb:
        lastTwo = getEnding(verb)
        ending = endings.get(lastTwo)
        conjugated = []
        for e in ending:
            conjugated += [verb.replace(lastTwo, e)]
        return conjugated
    else:
        return []

def firstPerson(sentence):
    s = sentence.lower().split()
    person, v = s[0], s[1]
    verb = getVerb(v)
    lastTwo = getEnding(verb)
    l = endings.get(lastTwo)
    c = conversion.get(person)
    newV = verb.replace(lastTwo, l[c[0]])
    return c[1] + " " + newV

print(getVerb("to buy"))
print(getVerb("to see"))
print(getEnding("comprar"))
print(getEnding("aprender"))
print()
print(conjugate("to buy"))
print(conjugate("to learn"))
print(conjugate("to see"))
print(firstPerson("I buy"))
print(firstPerson("You learn"))
def greenGlassDoor(word):
    lWord = word.lower()
    prevChar = lWord[0]
    for char in lWord[1:]:
        if char is prevChar:
            return True
        prevChar = char    
    return False

while 1 > 0:
    word = input("Give me a word and I'll tell you if it passes through the Green Glass Door: ")
    if word.lower() == "quit":
        break
    else:
        passes = greenGlassDoor(word)
        if passes:
            print(word + " passes through the Green Glass Door!")
        elif not passes:
            print(word +  " does not pass through the Green Glass Door.")

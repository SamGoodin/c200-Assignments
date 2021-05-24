def letter_to_code(letter):
    return code[letter]

space_between_letters = "..."

space_between_words = "......."

def word_to_code(word):
    newstr = ""
    letterCount = 0
    for letter in word:
        newstr += letter_to_code(letter)
        letterCount += 1
        if not(letterCount == len(word)):
            newstr += "..."
    return newstr

def sentence_to_code(s):
    sp = s.split()
    newstr = ""
    wordCount = 0
    for x in sp:
        newstr += word_to_code(x)
        wordCount += 1
        if not(wordCount == len(sp)):
            newstr += "......."
    return newstr

def code_to_letters(s):
    sp = s.split("...")
    newstr = ""
    for i in sp:
        for letter, morse in code.items():
            if i == morse:
                newstr += letter
    return newstr

def code_to_sentence(s):
    sp = s.split(".......")
    newstr = ""
    wordCount = 0
    for i in sp:
        newstr += code_to_letters(i)
        wordCount += 1
        if not (wordCount == len(sp)):
            newstr += " "
    return newstr


code = {
    'A': '=.===',
    'B': '===.=.=.=',
    'C': '===.=.===.=',
    'D': '===.=.=',
    'E': '=',
    'F': '=.=.===.=',
    'G': '===.===.=',
    'H': '=.=.=.=',
    'I': '=.=',
    'J': '=.===.===.===',
    'K': '===.=.===',
    'L': '=.===.=.=',
    'M': '===.===',
    'N': '===.=',
    'O': '===.===.===',
    'P': '=.===.===.=',
    'Q': '===.===.=.===',
    'R': '=.===.=',
    'S': '=.=.=',
    'T': '===',
    'U': '=.=.===',
    'V': '=.=.=.===',
    'W': '=.===.===',
    'X': '===.=.=.===',
    'Y': '===.=.===.===',
    'Z': '===.===.=.=',
    }

d = {}
for k,v in code.items():
    d[v] = k

def testing(s, c):
    if sentence_to_code(s) == c:
        print("S->C for {0} passed.".format(s))
    else:
        print("S->C for {0} failed.".format(s))
    if code_to_sentence(c) == s:
        print("C->S for {0} passed.".format(s))
    else:
        print("C->S for {0} failed.".format(s))

test_strings = ["MORSE CODE", "I NEED MONEY", "ORDER PIZZA"]
test_code = ['===.===...===.===.===...=.===.=...=.=.=...=.......===.=.===.=...===.===.===...===.=.=...=',
             '=.=.......===.=...=...=...===.=.=.......===.===...===.===.===...===.=...=...===.=.===.===',
             '===.===.===...=.===.=...===.=.=...=...=.===.=.......=.===.===.=...=.=...===.===.=.=...===.===.=.=...=.===']

for s,c in zip(test_strings, test_code):
    testing(s,c)

file = open("c.txt", 'r')
for line in file:
    print(code_to_sentence(line.strip()))
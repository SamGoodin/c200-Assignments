import numpy

#a = numpy.array()

b = open("c:\\users\\Sam\\Desktop\\data.txt", 'r')

for i in b:
    i = i.split(',')
    i[1] = i[1].rstrip()
    print(i)

import json

f = {
    "name": "Sam",
    "major": "Computer Science"
    }


with open('c:\\users\\Sam\\Desktop\\data.json', 'w') as fa:
    json.dump(f, fa, sort_keys=True, indent=2)

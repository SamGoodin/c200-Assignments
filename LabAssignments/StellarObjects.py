l = []
with open("Data.txt") as f:
    for line in f:
        l.append(line.split(';'))

k = {}
for i in l:
    k[i[0]] = [i[1].strip(), i[2].strip(), i[3].strip(), i[4].strip(), i[5].strip()]
del k["Stellar Object ID"]

'''max = k.get("1")
for key in k.keys():
    if k.get(key) > max:
        max = k.get(key)
        maxKey = key
print(max, maxKey)'''

def maxTemp(d):
    maxTemp = d.get('1')[1]
    for key in d.keys():
        if d.get(key)[1] > maxTemp:
            maxTemp = d.get(key)[1]
            maxKey = key
    return maxKey, maxTemp

def maxAge(d):
    maxAge = d.get('1')[2]

def maxMass(d):
    maxMass = d.get('1')[4]
    for key in d.keys():
        if d.get(key)[4] > maxMass:
            maxMass = d.get(key)[4]
            maxKey = key
    return maxKey, maxMass

print(maxTemp(k))
print(maxMass(k))

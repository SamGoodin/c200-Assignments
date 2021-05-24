def increase(l):
    o = []
    count = 0
    while count < len(l):
        startIdx = d = count
        flag = True
        while flag:
            if d == len(l) - 1:
                flag = False
            else:
                if l[d] <= l[d+1]:
                    d += 1
                else:
                    flag = False
        count += 1
        o.append([startIdx, d])
    g = 0
    idx = 0
    for i in o:
        m = i[1] - i[0]
        if m >= g:
            g = m
            idx = o.index(i)
    if g is 0:
        return []
    else:
        return l[o[idx][0]:o[idx][1] + 1]


print(increase([1, 2, 2, 1, 5, 2, 3, 4, 5, 8, 3]))
print(increase([7, 1, 7, 1, 8, 1]))
print(increase([1, 1, 5, 2, 2, 3, 3, 1]))
print(increase([5, 4, 3, 2, 1]))

def runOfOnes(l):
    o = []
    if not l:
        return 0
    elif len(l) is 1:
        if 0 in l:
            return 0
        elif 1 in l:
            return 1
    else:
        count = 0
        for i in l:
            if i is 1:
                if count is len(l) - 1:
                    pass
                else:
                    flag = True
                    d = 0
                    idx = count
                    while flag:
                        if l[idx] is 1:
                            d += 1
                            idx += 1
                        else:
                            flag = False
                    o.append(d)
            count += 1
        big = o[0]
        for i in o[1:]:
            if i > big:
                big = i
        return big

print(runOfOnes([1]))
print(runOfOnes([0,1,1,0,1,0,1,1,1,0,1,0,1]))
print(runOfOnes([1, 1, 1, 1, 1, 0, 1]))
print(runOfOnes([]))
print(runOfOnes([0]))

def stringIntersection(string1, string2):
    newStr = ""
    for i in string1:
        for x in string2:
            if x is i:
                newStr += x
    return newStr

print(stringIntersection("abcd325", "5tDEDc3"))
print(stringIntersection("Do0", "g30rtuD"))
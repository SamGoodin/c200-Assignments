'''
def ff(n):
    counter = 1
    num = 1
    while counter < (n + 1):
        num *= counter
        counter += 1
    return num

print(ff(5))
'''
x = [45, 1, 33, 41, 1, 45, 355]

def rf(xlst, y):
    for n in xlst:
        if n is y:
            xlst.remove(n)
    return xlst

print(rf(x, 1))

'''#List Manipulation
print(x + [59])
print([] + [])
print(x[1:] + x[:1
'''
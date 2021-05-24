import numpy as np

def r(x, y):
    xs = ys = xys = xss = yss = 0
    for i in x:
        xs += (i[0])
        xss += ((i[0]**2))
    for i in y:
        ys += (i[0])
        yss += ((i[0]**2))
    count = 0
    while count < 6:
        xys += ((x[count][0] * y[count][0]))
        count += 1
    i = (6 * xys) - (xs * ys)
    j = (((6 * xss - (xs**2)) * (6 * yss - (ys**2)))**0.5)
    return(i / j)


a = np.array(range(12), int).reshape((6, 2))

fm = open("studyhours.txt", 'r')

for i in range(6):
    d = fm.readline().split(",")
    a[i][0] = int(d[0])
    a[i][1] = int(d[1])

print("The correlation is: {0}.".format(r(a[:, [0]], a[:, [1]])))

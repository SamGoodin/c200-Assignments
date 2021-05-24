from timeit import default_timer as timer
import numpy as np

def fibRecursive(n):
    if n < 2:
        return n
    elif n >= 100:
        return n
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)

for n in range(1, 40, 10):
    start = timer()
    print("f({0}) = {1} took {2} seconds.".format(n, fibRecursive(n), timer() - start))

def fibForLoop(n):
    a = np.array(range(n+1), int)
    a[0] = 0
    a[1] = 1
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

for n in range(1, 80, 10):
    start = timer()
    print("f({0}) = {1} took {2} seconds.".format(n, fibForLoop(n), timer() - start))

#The numbers seem to change (roughly) by squaring the original
#number and then multiplying by 2.

#The for loop implementation is faster than the recursive
#implementation.
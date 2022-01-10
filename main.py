import sys
from time import time

data = []
n = 26
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4}'.format(a, b))
    data.append(None)  # increase len by one


def compute_average(n):
    data = []
    start = time()
    for i in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

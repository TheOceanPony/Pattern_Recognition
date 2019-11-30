import numpy as np


def recursive_strategy(x, histogram, y, t, prob):
    # print("step="+str(t)+"\n")
    res = np.zeros(9 * t + 1)
    prev = res
    p = conditional_prob(histogram, x[0], y, prob)
    prev[0:10] = p
    for i in range(1, t):
        p = conditional_prob(histogram, x[i], y, prob)
        res = np.zeros(9 * t + 1)
        for d in range(0, 9 * i + 1):
            for k in range(0, min(9 * (i + 1) - d + 1, 10)):
                res[d + k] += prev[d] * p[k]
        prev = res
    return np.array(res)


def conditional_prob(histogram, x, y, p):
    if p == 0:
        res = np.zeros(10)
        res[find(x, y)] = 1
        return res
    elif p == 1:
        res = np.zeros(10)
        res[find(invert(x), y)] = 1
        return res
    res = []
    for k in range(10):
        a = histogram[k]
        b = 0
        for i in range(10):
            b += histogram[i] * ((p / (1 - p)) ** (sum_xor(y[i], x) - sum_xor(y[k], x)))
        res.append(a / b)
    return np.array(res)


def generator(n, y, histogram):
    m = np.random.choice(10, size=n, p=histogram)
    res = translate(m, y)

    number = ""
    for i in range(len(m)):
        number += str(m[i])
    return [res, np.sum(m), number]


def upscale(y, scale):
    """
       >>> upscale([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1], 2)
       array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0,
              1, 1, 1, 1, 1, 1, 1, 1])
       >>> upscale([1, 2], 5)
       array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
    """
    res = []
    for i in range(0, len(y)):
        for j in range(0, scale):
            res.append(y[i])
    return np.array(res)


def translate(a, y):
    res = [None]*len(a)
    for i in range(len(a)):
        res[i] = y[a[i]]
    return res


def noised(y, prob):
    res = []
    for i in range(len(y)):
        res.append(xor(y[i], np.random.choice(2, size=len(y[i]), p=[1 - prob, prob])))
    return res


def argmax(arr):
    return np.argmax(arr)


def invert(arr):
    """
    invert(np.array([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]))
    array([0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

    """
    return 1 - arr


def find(x, y):
    """
    find(np.array([2]),np.array([3,1,2,4,3,7]))
    2
    find(np.array([1]),np.array([1,1,1,1,1,1,1]))
    0
    """
    for i in range(0, len(y)):
        if (x == y[i]).all():
            return i


def sum_xor(a, b):
    return np.sum(xor(a, b))


def xor(a, b):
    result = []
    for i in range(len(a)):
        result.append(int(a[i] != b[i]))
    return np.array(result)


y = [
    [1, 1, 1,  # 0
     1, 0, 1,
     1, 0, 1,
     1, 0, 1,
     1, 1, 1],

    [0, 1, 0,  # 1
     0, 1, 0,
     0, 1, 0,
     0, 1, 0,
     0, 1, 0],

    [1, 1, 1,  # 2
     0, 0, 1,
     1, 1, 1,
     1, 0, 0,
     1, 1, 1],

    [1, 1, 1,  # 3
     0, 0, 1,
     1, 1, 1,
     0, 0, 1,
     1, 1, 1],

    [1, 0, 1,  # 4
     1, 0, 1,
     1, 1, 1,
     0, 0, 1,
     0, 0, 1],

    [1, 1, 1,  # 5
     1, 0, 0,
     1, 1, 1,
     0, 0, 1,
     1, 1, 1],

    [1, 1, 1,  # 6
     1, 0, 0,
     1, 1, 1,
     1, 0, 1,
     1, 1, 1],

    [1, 1, 1,  # 7
     0, 0, 1,
     0, 1, 0,
     1, 0, 0,
     1, 0, 0],

    [1, 1, 1,  # 8
     1, 0, 1,
     1, 1, 1,
     1, 0, 1,
     1, 1, 1],

    [1, 1, 1,  # 9
     1, 0, 1,
     1, 1, 1,
     0, 0, 1,
     0, 0, 1],
]


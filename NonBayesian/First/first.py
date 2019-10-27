import numpy as np
from numpy.random import choice as generator


def random_histogram(n):
    res = np.random.rand(n)
    return res / np.sum(res)


# def generator(probability, length, k):
# return np.random.choice(k, length, p=probability)


def square_penalty(k, weight, j):
    res = 0
    for i in range(0, len(k)):
        res += weight[i] * (k[i] - k[j]) ** 2
    return res


def binary_penalty(k, weight, j):
    res = 0
    for i in range(0, len(k)):
        res += weight[i] * (int(k[j] != k[i]))
    return res


def square_strategy(k, histogram):
    res = 0
    minimum = square_penalty(k, histogram, 0)
    for j in range(1, len(k)):
        a = square_penalty(k, histogram, j)
        if a < minimum:
            minimum = a
            res = j
    return [res, k[res]]


def binary_strategy(k, histogram):
    res = 0
    minimum = binary_penalty(k, histogram, 0)
    for j in range(1, len(k)):
        a = binary_penalty(k, histogram, j)
        if a < minimum:
            minimum = a
            res = j
    return [res, k[res]]


def nonbayesian_penalty(k, histogram, alpha, j):
    res = -alpha * histogram[j]
    for i in range(0, len(k)):
        res = res + histogram[i] * ((k[j] - k[i]) ** 2)
    return res


def nonbayesian_strategy(k, histogram, alpha):
    res = 0
    minimum = nonbayesian_penalty(k, histogram, alpha, 0)
    for j in range(1, len(k)):
        a = nonbayesian_penalty(k, histogram, alpha, j)
        if a < minimum:
            minimum = a
            res = j
    return k[res]


def binary_risk(k, histogram):
    risk1 = 0
    risk2 = 0
    for j in range(0, 10 ** 4):
        k0 = generator(k, 1, p=histogram)[0]
        risk1 += int((binary_strategy(k, histogram)[1]) != k0)
        risk2 += int((square_strategy(k, histogram))[1] != k0)
    return [risk1 / (10 ** 4), risk2 / (10 ** 4)]


def square_risk(k, histogram):
    risk1 = 0
    risk2 = 0
    for j in range(0, (10 ** 4)):
        k0 = generator(k, 1, p=histogram)[0]
        risk1 += ((square_strategy(k, histogram)[1] - k0) ** 2)
        risk2 += ((binary_strategy(k, histogram)[1] - k0) ** 2)

    return [risk1 / (10 ** 4), risk2 / (10 ** 4)]


k = np.array([10, 20, 30, 40, 50])
histogram = np.array([0.1, 0.4, 0.2, 0.1, 0.2])

print(f"binary risk {binary_risk(k, histogram)}")
print(f"binary_penalty {[binary_penalty(k, histogram, binary_strategy(k, histogram)[0]), binary_penalty(k, histogram, square_strategy(k, histogram)[0])]}")


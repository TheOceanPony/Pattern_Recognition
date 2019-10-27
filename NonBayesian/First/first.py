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
    return [res,k[res]]


def binary_risk(k):
  risk=np.array([0, 0, 0])
  res=np.array([0, 0, 0])
  for i in range (0, 10**4):
    histogram=random_histogram(len(k))
    k0=generator(k, 10**4, p=histogram)
    res[0]=binary_strategy(k, histogram)[1]
    res[1]=square_strategy(k, histogram)[1]
    res[2]=nonbayesian_strategy(k, histogram,10000)[1]
    for j in range(0, 10**4):
      risk[0]+=int(res[0]!=k0[j])
      risk[1]+=int(res[1]!=k0[j])
      risk[2]+=int(res[2]!=k0[j])
    risk=risk/(10**4)
  return (risk/(10**4))

def square_risk(k):
  risk=np.array([0, 0, 0])
  res=np.array([0, 0, 0])
  for i in range (0, 10**4):
    histogram=random_histogram(len(k))
    k0=generator(k, 10**4, p=histogram)
    res[0]=square_strategy(k, histogram)[1]
    res[1]=binary_strategy(k, histogram)[1]
    res[2]=nonbayesian_strategy(k, histogram,1000)[1]
    for j in range(0, 10**4):
      risk[0]+=((res[0]-k0[j])**2)
      risk[1]+=((res[1]-k0[j])**2)
      risk[2]+=((res[2]-k0[j])**2)
    risk=risk/(10**4)
  return (risk/(10**4))


k = np.array([10, 20, 30, 40, 50])
histogram = np.array([0.1, 0.4, 0.2, 0.1, 0.2])

print(f"binary risk {binary_risk(k)}")
print(f"binary_penalty {[binary_penalty(k, histogram, binary_strategy(k, histogram)[0]), binary_penalty(k, histogram, square_strategy(k, histogram)[0])]}")


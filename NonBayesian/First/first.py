import numpy as np
from numpy.random import choice as generator
import matplotlib.pyplot as plt

def random_histogram(n):
    res = np.random.rand(n)
    return res / np.sum(res)


# def generator(probability, length, k):
# return np.random.choice(k, length, p=probability)


def square_penalty(k, weight, j):
    """
        >>> [square_penalty([10, 20, 30, 40, 50],[0.1, 0.4, 0.2, 0.1, 0.2], i) for  i in range(0,5)]
        [530.0, 250.0, 170.0, 290.0, 610.0]
        """
    res = 0
    for i in range(0, len(k)):
        res += weight[i] * (k[i] - k[j]) ** 2
    return res


def binary_penalty(k, weight, j):
    """
            >>> [binary_penalty([50, 13, 21, 48, 16],[0.7, 0.1, 0.1, 0.05, 0.05], i) for  i in range(0,5)]
            [0.3, 0.9, 0.9, 0.95, 0.95]
            """
    res = 0
    for i in range(0, len(k)):
        res += weight[i] * (int(k[j] != k[i]))
    return res


def square_strategy(k, histogram):
    """
                >>> square_strategy([50, 13, 21, 48, 16, 79],[0.3, 0.1, 0.1, 0.05, 0.05, 0.4])
                [0, 50]
                """
    res = 0
    minimum = square_penalty(k, histogram, 0)
    for j in range(1, len(k)):
        a = square_penalty(k, histogram, j)
        if a < minimum:
            minimum = a
            res = j
    return [res, k[res]]


def binary_strategy(k, histogram):
    """
                    >>> binary_strategy([50, 13, 21, 48, 16, 79],[0.3, 0.1, 0.1, 0.05, 0.05, 0.4])
                    [5, 79]
                    """
    res = 0
    minimum = binary_penalty(k, histogram, 0)
    for j in range(1, len(k)):
        a = binary_penalty(k, histogram, j)
        if a < minimum:
            minimum = a
            res = j
    return [res, k[res]]


def nonbayesian_penalty(k, histogram, alpha, j):
    """
                        >>> [nonbayesian_penalty([155, 98, 12, 48, 16, 0.3],[0.5, 0.05, 0.1, 0.05, 0.1, 0.2], 10, i) for i in range(0,6)]
                        [9493.318, 5070.058, 10687.078, 6536.058, 10097.798000000003, 12593.411999999997]
                        """
    res = -alpha * histogram[j]
    for i in range(0, len(k)):
        res = res + histogram[i] * ((k[j] - k[i]) ** 2)
    return res


def nonbayesian_strategy(k, histogram, alpha):
    """
                            >>> nonbayesian_strategy([155, 98, 12, 48, 16, 0.3, -9],[0.2, 0.05, 0.1, 0.05, 0.1, 0.3, 0.2], 10)
                            [3, 48]
                            """
    res = 0
    minimum = nonbayesian_penalty(k, histogram, alpha, 0)
    for j in range(1, len(k)):
        a = nonbayesian_penalty(k, histogram, alpha, j)
        if a < minimum:
            minimum = a
            res = j
    return [res,k[res]]


def binary_risk(k, q, alpha=None):
  risk=0
  res=0
  for i in range (0, 10**4):
    histogram=random_histogram(len(k))
    k0=generator(k, 10**4, p=histogram)
    if(alpha is None):
      res=(q(k,histogram)[0])
    else:
      res=(q(k,histogram, alpha)[0])
    risk+=binary_penalty(k, histogram, res)
    # risk/(10**4)
  return (risk/(10**4))

def square_risk(k, q, alpha=None):
  risk=0
  res=0
  for i in range (0, 10**4):
    histogram=random_histogram(len(k))
    k0=generator(k, 10**4, p=histogram)
    if(alpha is None):
      res=(q(k,histogram)[0])
    else:
      res=(q(k,histogram, alpha)[0])
    risk+=square_penalty(k, histogram, res)
    # risk=risk/(10**4)
  return (risk/(10**4))


def conditional_risk(k, q, histogram, alpha=None):
  risk=np.array([0,0])
  res=0
  k0=generator(k, 10**5, p=histogram)
  if(alpha is None):
      res=(q(k,histogram)[1])
  else:
      res=(q(k,histogram, alpha)[1])
  for j in range(0, 10**5):
    risk[0]+=((res-k0[j])**2)
    risk[1]+=int(res!=k0[j])
  return (risk/(10**5))

k = np.array([10, 20, 30, 40, 50])
histogram = np.array([0.1, 0.2, 0.1, 0.4, 0.2])
print(nonbayesian_strategy([155, 98, 12, 48, 16, 0.3, -9],[0.2, 0.05, 0.1, 0.05, 0.1, 0.3, 0.2], 10))
"""
#Building a plot
 
cond_bin = []
cond_nb = []
a = []

for alpha in range(0, 10**4, 50):
  a.append(alpha)
  cond_bin.append(conditional_risk(k, binary_strategy, histogram, None)[1] )
  cond_nb.append(conditional_risk(k, nonbayesian_strategy, histogram, alpha)[1] )

plt.plot(a, cond_bin, 'r--', a, cond_nb, 'b--')
plt.xlabel('alpha')
plt.ylabel('binary (red) & nonbayesian (blue)')
plt.show()
"""

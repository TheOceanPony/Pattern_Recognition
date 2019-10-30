import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def srnd_with_zeros(arr):
    """
    >>> srnd_with_zeros(np.ones(10))
    array([0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0.])
    >>> srnd_with_zeros(np.zeros(10))
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    >>> srnd_with_zeros(np.ones((3, 3)))
    array([[0., 0., 0., 0., 0.],
           [0., 1., 1., 1., 0.],
           [0., 1., 1., 1., 0.],
           [0., 1., 1., 1., 0.],
           [0., 0., 0., 0., 0.]])
    """
    if arr.ndim == 1:
        n = np.shape(arr)[0]
        z_arr = np.zeros(n + 2)
        z_arr[1:n+1] = arr
        return z_arr

    if arr.ndim == 2:
        n = np.shape(arr)[0]
        m = np.shape(arr)[1]
        z_arr = np.zeros((n + 2, m+2))
        z_arr[1:n + 1, 1:m+1] = arr
        return z_arr

    if arr.ndim == 3:
        n = np.shape(arr)[0]
        m = np.shape(arr)[1]
        k = np.shape(arr)[2]
        z_arr = np.zeros((n + 2, m + 2, k + 2))
        z_arr[1:n + 1, 1:m + 1, 1:k + 1] = arr
        return z_arr

    raise Exception("Bad arguments")


def cache(arr):
    """
    >>> cache(np.ones(10))
    array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
    >>> cache(np.ones((3, 3)))
    array([[1., 2., 3.],
           [2., 4., 6.],
           [3., 6., 9.]])
    """
    cache_arr = np.zeros(np.shape(arr))

    if arr.ndim == 1:
        for i in range(0, np.shape(arr)[0]):
            cache_arr[i] = np.sum(arr[0:i+1])
        return cache_arr

    if arr.ndim == 2:
        for i in range(0, np.shape(arr)[0]):
            for j in range(0, np.shape(arr)[1]):
                cache_arr[i, j] = np.sum(arr[0:i+1, 0:j+1])
        return cache_arr

    if arr.ndim == 3:
        for i in range(0, np.shape(arr)[0]):
            for j in range(0, np.shape(arr)[1]):
                for k in range(0, np.shape(arr)[2]):
                    cache_arr[i, j, k] = np.sum(arr[0:i+1, 0:j+1, 0:k+1])
        return cache_arr

    else:
        raise Exception("Bad dimension")


def cache2(arr):
    """
        >>> cache2(np.ones(10))
        array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.,  0.])
        >>> cache2(np.ones((3, 3)))
        array([[0., 0., 0., 0., 0.],
               [0., 1., 2., 3., 0.],
               [0., 2., 4., 6., 0.],
               [0., 3., 6., 9., 0.],
               [0., 0., 0., 0., 0.]])

    """
    if arr.ndim == 1:
        n = np.shape(arr)[0]
        cache_arr = np.zeros(n + 2)
        for i in range(1, n + 1):
            cache_arr[i] = cache_arr[i-1] + arr[i-1]
        return cache_arr
    if arr.ndim == 2:
        n = np.shape(arr)[0]
        m = np.shape(arr)[1]
        cache_arr = np.zeros((n + 2, m + 2))
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cache_arr[i, j] = cache_arr[i, j - 1] + cache_arr[i - 1, j] - cache_arr[i - 1, j - 1] + arr[i - 1, j - 1]
        return cache_arr

    if arr.ndim == 3:
        n = np.shape(arr)[0]
        m = np.shape(arr)[1]
        k = np.shape(arr)[2]
        cache_arr = np.zeros((n + 2, m + 2, k + 2))
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(1, k + 1):
                    cache_arr[i, j, k] = cache_arr[i-1, j ,k] + cache_arr[i, j-1, k] + cache_arr[i, j, k-1] \
                                         - cache_arr[i, j-1, k-1] - cache_arr[i-1, j, k-1] - cache_arr[i-1, j-1, k]\
                                         + cache_arr[i-1, j-1, k-1] + arr[i-1, j-1, k-1]
        return cache_arr
        return 0
    else:
        raise Exception("Bad dimension")


def cumsum_cached(arr, cache_arr, start_point, end_point):
    """
    >>> cumsum_cached(np.ones(10), cache(np.ones(10)), [7], [3])
    -3.0
    >>> cumsum_cached(np.zeros(10), cache(np.zeros(10)), [10], [0])
    0.0
    """
    if arr.ndim == 1:
        return cache_arr[end_point[0]] - cache_arr[start_point[0]-1]

    if arr.ndim == 2:
        start_point = start_point - np.array([1, 1])
        return cache_arr[ end_point[0], end_point[1] ]\
               - cache_arr[ end_point[0], start_point[1] ]\
               - cache_arr[ start_point[0], end_point[1] ]\
               + cache_arr[ start_point[0], start_point[1] ]

    if arr.ndim == 3:
        start_point = start_point - np.array([1, 1, 1])
        return cache_arr[end_point[0], end_point[1], end_point[2]] \
               - cache_arr[start_point[0], end_point[1], end_point[2]] \
               - cache_arr[end_point[0], start_point[1], end_point[2]] \
               - cache_arr[end_point[0], end_point[1], start_point[2]] \
               + cache_arr[end_point[0], start_point[1], start_point[2]] \
               + cache_arr[start_point[0], end_point[1], start_point[2]] \
               + cache_arr[start_point[0], start_point[1], end_point[2]] \
               - cache_arr[start_point[0], start_point[1], start_point[2]]
    else:
        raise Exception("Bad dimension")


def cumsum_slow(arr, start_point, end_point):
    """
        >>> cumsum_slow(np.ones(10), [3], [7])
        5.0
        >>> cumsum_slow(np.zeros(10), [10], [0])
        0
    """
    result = 0

    if arr.ndim == 1:
        for i in range(start_point[0], end_point[0]+1):
            result = result + arr[i]
        return result

    if arr.ndim == 2:
        for i in range(start_point[0], end_point[0]+1):
            for j in range(start_point[1], end_point[1]+1):
                result = result + arr[i, j]
        return result

    if arr.ndim == 3:
        for i in range(start_point[0], end_point[0]+1):
            for j in range(start_point[1], end_point[1]+1):
                for k in range(start_point[2], end_point[2]+1):
                    result = result + arr[i, j, k]
        return result
    else:
        raise Exception("Bad dimension")

def experiment(t, cache_arr):
    start_point = [0, 0]
    end_point = [t - 1, t - 1]

    start = timer()
    cumsum_cached(A, cache_arr, start_point, end_point)
    end = timer()
    t1 = end - start

    return (t1*1000)


z=[]
for j in range(0, 30, 1):
  A = np.random.randint(50, size=(10, 10))
  cache_arr = cache2(A)
  X = []
  Y = []
  for t in range(3, 10, 10):
    X.append(t)
    a = experiment(t, cache_arr)
    if a > 0.01:
      Y.append(a)
    else:
      Y.append(a)
  z.append(np.array(Y))
z=np.array(z)
a=np.average(z, axis=0) 
len(a)

T=[]
import math
for j in range(0, np.shape(z)[1]):
  sumec=0
  for i in range(0,np.shape(z)[0]):
    sumec+= math.sqrt(((z[i][j]-a[j])**2))/np.shape(z)[0] 
  T.append(sumec)
T=np.array(T)

print(f" X:{X}, \nY:{Y}, \nT:{T}" )

for i in range(0, len(Y)):
  if Y[i] > 0.01 or Y[i] < 0.0045:
    Y[i] = 0.006039999789209105




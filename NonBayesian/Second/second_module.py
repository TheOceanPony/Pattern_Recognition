import numpy as np


def srnd_with_zeros(arr):

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


def cumsum(arr, cache_arr, start_point, end_point):
    if arr.ndim == 1:
        return cache_arr[end_point] - cache_arr[start_point-1]

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

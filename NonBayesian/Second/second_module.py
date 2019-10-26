import numpy as np
# TODO description for all functions


def num_sum(arr, end_point, start_point=(0, 0, 0)):
    """
    :param arr: numpy array
    :param start_point:
    :param end_point:
    :return: the sum of all elements that are in this 'slice'

    This function is mainly for code consistency
    """
    if arr.ndim == 1:
        return np.sum(arr[ start_point[0]:end_point[0] + 1])
    if arr.ndim == 2:
        return np.sum(arr[ start_point[0]:end_point[0] + 1, start_point[1]:end_point[1] + 1 ])
    if arr.ndim == 3:
        return np.sum(arr[ start_point[0]:end_point[0] + 1, start_point[1]:end_point[1] + 1, start_point[2]:end_point[2] + 1 ])
    else:
        raise Exception("Bad dimension")


def cache(arr):
    """
    :param arr: numpy array
    :return: array of all particial-sums
    """

    cache_arr = np.zeros(np.shape(arr))

    if arr.ndim == 1:
        for i in range(0, np.shape(arr)[0]):
            cache_arr[i] = num_sum(arr, [i])
        return cache_arr

    if arr.ndim == 2:
        for i in range(0, np.shape(arr)[0]):
            for j in range(0, np.shape(arr)[1]):
                cache_arr[i, j] = num_sum(arr, (i, j))
        return cache_arr

    if arr.ndim == 3:
        for i in range(0, np.shape(arr)[0]):
            for j in range(0, np.shape(arr)[1]):
                for k in range(0, np.shape(arr)[2]):
                    cache_arr[i, j, k] = num_sum(arr, (i, j, k))
        return cache_arr

    else:
        raise Exception("Bad dimension")


def cum_sum(arr, cache_arr, end_point, start_point):
    # TODO ndim == 3 case

    if arr.ndim == 1:
        return cache_arr[end_point] - cache_arr[start_point]
    if arr.ndim == 2:
        return cache_arr[end_point[0], end_point[1]]\
               - cache_arr[end_point[0], start_point[1]-1]\
               - cache_arr[start_point[0]-1, end_point[1]]\
               + cache_arr[start_point[0]-1, start_point[1]-1]
    if arr.ndim == 3:
        return
    else:
        raise Exception("Bad dimension")






# TODO implement colored answers --(low priority)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Test" + bcolors.ENDC)
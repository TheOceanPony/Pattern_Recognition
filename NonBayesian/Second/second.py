import numpy as np
import second_module as I
from timeit import default_timer as timer


def experiment(t):
    A = np.ones((t, t, t))
    start_point = [0, 0, 0]
    end_point = [t - 1, t - 1, t - 1]
    cache_arr = I.cache2(A)

    start = timer()
    I.cumsum_cached(A, cache_arr, start_point, end_point)
    end = timer()
    t1 = end - start

    start = timer()
    I.cumsum_slow(I.srnd_with_zeros(A), start_point, end_point)
    end = timer()
    t2 = end - start
    return (t1*1000)/t


for t in range(10, 1000):
    print(f"{t} - {experiment(t)}")

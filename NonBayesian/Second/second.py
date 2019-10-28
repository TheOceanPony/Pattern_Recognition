import numpy as np
import second_module as I
from timeit import default_timer as timer

"""
1
A = np.ones(10)
start_point = 0
end_point = 3

2
A = np.ones((5, 5))
start_point = [1, 1]
end_point = [3, 3]  

3
A = np.ones((3, 3, 3))
start_point = [1, 1, 1]
end_point = [3, 3, 3]  

3
A = np.random.randint(255, size=(100, 100, 100))
start_point = [12, 14, 21]
end_point = [67, 58, 90]
"""
A = np.random.randint(255, size=(10, 10, 10))
start_point = [1, 0, 1]
end_point = [8, 5, 6]

cache_arr = I.srnd_with_zeros(I.cache(A))
print(f"A\n{A} \n\nCache\n{cache_arr}")
start = timer()
print(f"cached sum: {I.cumsum_cached(A, cache_arr, start_point, end_point)}")
end = timer()
print(end - start)
start = timer()
print(f"slow sum: {I.cumsum_slow(I.srnd_with_zeros(A), start_point, end_point)}")
end = timer()
print(end - start)

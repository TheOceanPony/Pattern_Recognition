import numpy as np
import second_module as I

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
"""
A = np.ones((3, 3, 3))
start_point = [0, 0, 0]
end_point = [3, 3, 3]

cache_arr = I.srnd_with_zeros(I.cache(A))
print(f"A\n{A} \n\nCache\n{cache_arr}")
print(f"cached sum: {I.cumsum_cached(A, cache_arr, start_point, end_point)}")
print(f"slow sum: {I.cumsum_slow(I.srnd_with_zeros(A), start_point, end_point)}")
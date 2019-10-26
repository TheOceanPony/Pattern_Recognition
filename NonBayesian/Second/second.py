import numpy as np
import second_module as I

"""
B = np.ones((5, 5))
B = np.random.randint(10, size=20)
B = np.random.randint(10, size=(10, 10))
B = np.array([1, 2, 3, 4, 5, 6])
B = np.array([[10, 10, 10, 10, 10, 10],
              [10, 1, 1, 1, 1, 10],
              [10, 1, 1, 1, 1, 10],
              [10, 10, 10, 10, 10, 10]])
"""

B = np.ones((5, 5))
start_point = (1, 1)
end_point = (3, 5)

print(B)
cache_arr = I.cache(B)
print(cache_arr)
print(I.cum_sum(B, cache_arr, (4, 4), (3, 3) ))
print(I.num_sum(B, (4, 4), (3, 3) ))

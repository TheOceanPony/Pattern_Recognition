from functions import *
import time

NUMBER_LENGTH = 21
SCALE = 20
NOISE = 0.3
HISTOGRAM = [0.15, 0.2, 0.1, 0.05, 0.1, 0.05, 0.1, 0.05, 0.1, 0.1]
REPEATS = 1

# Upscaling
for i in range(0, len(y)):
    y[i] = upscale(y[i], SCALE)

j = 0
start = time.time()
# Computing
for i in range(0, REPEATS):
    k = generator(NUMBER_LENGTH, y, HISTOGRAM)
    x = noised(k[0], NOISE)
    res = recursive_strategy(x, HISTOGRAM, y, NUMBER_LENGTH, NOISE)

    if argmax(res) == k[1]:
        j += 1

    print(f"{i} | {k[2]} | {argmax(res)%3 == 0}")

end = time.time()
print(f"================== \n Success rate: {j}/{REPEATS} \n Time: {end-start} sec")


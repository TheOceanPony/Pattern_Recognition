import math
# TODO write a description for each function


def parse_even(arr, index=0):
    result = []
    for i in range(index, len(arr)):
        if i % 2 == 0:
            result.append(arr[i])
    return result


def parse_odd(arr, index=0):
    result = []
    for i in range(index, len(arr)):
        if i % 2 != 0:
            result.append(arr[i])
    return result
        

def glossary(arr, symbols_amount, length):
    glossary = []
    for w in range(0, symbols_amount):
        glossary.append([])
    i = 0
    for t in range(0, len(arr) - 1, length + 1):
        for d in range(t+1, t + length + 1):
            glossary[i].append(arr[d])
        i += 1
    return glossary


def max_index(arr):
    maximum = arr[0]
    max_ind = 0
    for i in range(1, len(arr)):
        if maximum < arr[i]:
            maximum = arr[i]
            max_ind = i
    return max_ind


def compare(arr_x, arr_y, p):
    if len(arr_x) != len(arr_y):
        return -404
    prod = 0
    for i  in range(0, len(arr_x) ):
        prod += (arr_x[i] != arr_y[i])*math.log(p) + (1 != (arr_x[i] != arr_y[i]))*math.log(1 - p)
    return prod



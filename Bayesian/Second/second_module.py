def parse(_string):
    temp = _string.split('\n')
    temp = temp[1].split(' ')

    for i in range(0, len(temp)):
        temp[i] = int(temp[i])
    return temp


def normalise(_heatmap):
    '''
    >>> normalise([201, 177, 187, 178, 167, 168, 147, 155, 150, 158, 158, 150])
    [0.10070140280561123, 0.08867735470941884, 0.093687374749499, 0.08917835671342686, 0.08366733466933868, 0.0841683366733467, 0.07364729458917836, 0.07765531062124248, 0.07515030060120241, 0.07915831663326653, 0.07915831663326653, 0.07515030060120241]
    '''
    total = sum(_heatmap)

    for i in range(0, len(_heatmap)):
        _heatmap[i] = _heatmap[i] / total

    return _heatmap


def predict_L1(_heatmap):
    total = 0
    for i in range(0, len(_heatmap)):
        if total >= 0.5:
            return i-1
        total += _heatmap[i]
    return "!ERROR! - bad heatmap"


def predict_delta(_heatmap, _delta):
    temp = []
    for i in range(_delta, len(_heatmap) - _delta):
        temp.append(Isum(_heatmap, i-_delta, i+_delta))

    answer = maxInd(temp) + _delta
    return answer

# TODO a replacement to this...nonsense
def Isum(_arr,  _start=0, _end=-1):
    if _start > _end:
        return f"Error: _end: {_end} is less that _start: {_start}";
    total = 0
    for i in range(_start, _end+1):
        total += _arr[i]
    return total


def maxInd(_arr):
    """
    >>> maxInd([1 ,2, 3, 4, 5, 6])
    5
    >>> maxInd([1 ,2, 3, 4, 5,-6])
    4
    >>> maxInd([1, 2, 0, 2, 1])
    1
    """
    maximum = _arr[0]
    max_ind = 0
    for i in range(1, len(_arr)):
        if maximum < _arr[i]:
            maximum = _arr[i]
            max_ind = i
    return max_ind



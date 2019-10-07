#Parsing heatmap
def Parse(_string):
	temp = _string.split('\n')
	temp = temp[1].split(' ')

	for i in range (0, len(temp)):
		temp[i] = int(temp[i])
	#print(temp)
	return temp;


#Normalising heatmap
def Normalise(_heatmap):
	total = sum(_heatmap)

	for i in range(0, len(_heatmap)):
		_heatmap[i] = _heatmap[i] / total

	return _heatmap;

#Strategy when loss = L1
def predictL1(_heatmap):
	sum = 0
	for i in range(0, len(_heatmap)):
		if (sum >= 0.5):
			return i-1;
		sum += _heatmap[i]
	return "!ERROR! - bad heatmap"; 


#Strategy when loss is integer
def predictDelta(_heatmap, _delta):
	temp = []
	for i in range( _delta, len(_heatmap) - _delta):
		temp.append( Isum(_heatmap, i-_delta, i+_delta))


	answer = maxInd(temp) + _delta
	return answer;

#Just a custom sum function 'cause I can
def Isum(_arr,  _start=0, _end=-1):
	if (_start > _end): return f"Error: _end: {_end} is less that _start: {_start}";

	sum = 0
	for i in range(_start, _end+1):
		sum += _arr[i]
	return sum;

#Return the index of the max element in array
def maxInd(_arr):
	max = _arr[0]
	maxInd = 0
	for i in range(1, len(_arr)):
		if (max < _arr[i]):
			max = _arr[i]
			maxInd = i
	return maxInd;



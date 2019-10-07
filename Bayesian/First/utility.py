import math

#---Displaying--- 
def show(arr, horScale): 
	arrWidth = 3*horScale
	k = 1
	for i in range(0,len(arr),arrWidth):
		for j in range(i,i+arrWidth-1):
			print(arr[j], end =' ')
		print(arr[arrWidth*k - 1])
		k += 1



#---Parsing---
def parseEven(arr, index = 0):
  result = []
  for i in range(index, len(arr)):
    if (i % 2 == 0): result.append(arr[i])
  return result;
        
#--Making & filling the dictionary
def dictionary(arr, symbolsAmount, length,):
  dictionary = []           
  for w in range(0,symbolsAmount):      #Creating the dictionary of right size
    dictionary.append([])

  i = 0
  for t in range(0,len(arr) - 1, length + 1):     #Filling it
    for d in range(t+1, t + length + 1):
      dictionary[i].append(arr[d])
    i += 1
  return dictionary;




#---MaxElementIndex---
def maxInd(arr):
    max = arr[0]
    maxInd = 0
    for i in range(1, len(arr)):
        if (max < arr[i]):
            max = arr[i]
            maxInd = i
    return maxInd;


#---Upscaling Rows---
def UpScaleRowS(arr, scale, width = 3):
	Rows = []
	for k in range(0,len(arr), width):
		tempRow = []

		for g in range(0,width):
			temp = [arr[k+g]]
			tempRow += temp*scale
		Rows.append(tempRow)
	return Rows;

#---Upscaling Array---
def UpScale(arr, horScale, verScale, width = 3, height = 5):
	arrUpS = []
	Rows = UpScaleRowS(arr, horScale)
	#print(Rows)
	for i in range(0, height):
			arrUpS += Rows[i] * verScale
	return arrUpS;

#---Xor--
def XorEl(A, B):
    return (A != B);

def XorArr(arr1, arr2):
    result = []

    for i in range(0, len(arr1)):
        result.append(XorEl(arr1[i], arr2[i]))

    return result;

#---Compare--
def compare(arrX, arrY, p):
    if ( len(arrX) != len(arrY)):
        return -404;
    prod = 0
    for i  in range(0, len(arrX) ):
            prod +=  XorEl(arrX[i], arrY[i])*math.log(p) + (XorEl("1", XorEl(arrX[i], arrY[i]))*math.log(1-p) )
    return prod;



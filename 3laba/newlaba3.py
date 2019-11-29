# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt

def xor(a,b):
  res=[]
  for i in range(len(a)):
    res.append(int(a[i]!=b[i]))
  return np.array(res)

def sum_xor(a,b):
  return np.sum(xor(a,b))

def conditional_prob(histogram, x,y,p):
  if p == 0:
        res = np.zeros(10)
        res[find(x, y)] = 1
        return res
  elif p == 1:
      res = np.zeros(10)
      res[find(invert(x), y)] = 1
      return res
  res=[]
  for k in range(10):
    a=histogram[k]
    b=0
    for i in range(10):
      b+=histogram[i]*((p/(1-p))**(sum_xor(y[i],x)-sum_xor(y[k],x)))
    res.append(a/b)
  return np.array(res)

def translate(a, y):
  res=[]
  for i in range(len(a)):
    res.append(y[a[i]])
  return res

def generator(n, y,histogram):
  m=np.random.choice(10, size=n, p=histogram)
  res=translate(m,y)
  return [res, np.sum(m)]

def upscale(y, scale):
  res=[]
  for i in range(0, len(y)):
    for j in range(0, scale):
      res.append(y[i])
  return np.array(res)

def find(x, y):
    for i in range(0, len(y)):
        if (x == y[i]).all():
            return i


def invert(arr):
    return 1 - arr


def recursive_strategy(x,histogram,y, t,prob):
  #print("step="+str(t)+"\n")
  res=np.zeros(9*t+1)
  prev=res
  p=conditional_prob(histogram,x[0],y,prob)
  prev[0:10]=p
  for i in range(1,t):
      p = conditional_prob(histogram, x[i], y, prob)
      res = np.zeros(9 * t + 1)
      for d in range(0,9*i+1):
          for k in range(0, min(9*(i+1)-d+1,10)):
            res[d+k]+=prev[d]*p[k]
      prev=res
  return np.array(res)

y=[[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1]]
y.append([0,1,0,0,1,0,0,1,0,0,1,0,0,1,0])
y.append([1,1,1,0,0,1,1,1,1,1,0,0,1,1,1])
y.append([1,1,1,0,0,1,1,1,1,0,0,1,1,1,1])
y.append([1,0,1,1,0,1,1,1,1,0,0,1,0,0,1])
y.append([1,1,1,1,0,0,1,1,1,0,0,1,1,1,1])
y.append([1,1,1,1,0,0,1,1,1,1,0,1,1,1,1])
y.append([1,1,1,0,0,1,0,1,0,1,0,0,1,0,0])
y.append([1,1,1,1,0,1,1,1,1,1,0,1,1,1,1])
y.append([1,1,1,1,0,1,1,1,1,0,0,1,0,0,1])

def noised(y, prob):
  res=[]
  for i in range(len(y)):
    res.append(xor(y[i],np.random.choice(2, size=len(y[i]), p=[1-prob,prob])))
  return res

for i in range(0, len(y)):
  y[i]=upscale(y[i], 20)
prob=0.1
histogram=[0.15,0.2,0.1,0.05,0.1,0.05,0.1,0.05,0.1,0.1]
j=0
for i in range(0, 10):
  k=generator(10, y, histogram)
  x=noised(k[0],prob)
  res=recursive_strategy(x, histogram, y, 10, prob)
  if(np.argmax(res)==k[1]):
    j+=1
  print(j)
j
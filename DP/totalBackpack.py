'''
total backpack
item can put to pack for 0 to unlimited times
'''

import sys
def totalPackUpdate(v, w, Target, arr):
  for weight in xrange(w, Target+1):
    arr[weight] = max(arr[weight], arr[weight-w] + v)

def totalPack(V,W,Target):
  arr = [0] * (Target+1)
  arr = [-sys.maxint-1] * (Target+1)
  arr[0] = 0
  for i in xrange(len(V)):
    totalPackUpdate(V[i], W[i], Target, arr)
  return arr


target = 5
V = [10,5,7,6,3]
W = [2,3,2,3,1]
print totalPack(V, W, target)
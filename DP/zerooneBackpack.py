'''
Zero-one backpack
'''
import sys
def zeroOneUpdate(v, w, arr, Target):
  for weight in xrange(Target, w-1, -1):
    arr[weight] = max(arr[weight], arr[weight-w]+v)


def zeroOneBackPack(V, W, Target):
  arr = [0] * (Target+1) # init to all zero --> any combination not over Target is valid
  arr = [-sys.maxint-1] * (Target+1) # init to all zero --> only combination equal to Target is valid
  arr[0] = 0
  for i in xrange(len(W)):
    zeroOneUpdate(V[i], W[i], arr, Target)
  return arr

target = 5
V = [10,5,7,6,3]
W = [1,3,2,3,1]
print zeroOneBackPack(V, W, target)
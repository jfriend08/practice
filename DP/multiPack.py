'''
Multi-pack
each item is limited, can can put into pack for 0 to limited times
'''

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

def multiPackUpdate(v, w, m, Target, arr, V, W):
  print v, w, m
  if w*m >= Target:
    totalPackUpdate(v, w, Target, arr)
  else:
    k = 1
    while k < m:
      zeroOneUpdate(k*v, k*w, arr, Target)
      m = m - k
      k = 2*k

def multiPack(V, W, M, Target):
  arr = [0] * (Target+1)
  for i in xrange(len(V)):
    multiPackUpdate(V[i], W[i], M[i], Target, arr, V, W)
    print arr
  return arr


target = 5
V = [10,5,7,6,6]
W = [1,3,2,3,1]
M = [2,2,3,1,2]

multiPack(V, W, M, target)
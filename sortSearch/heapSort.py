'''
Heap Sort
'''

from heapq import *
def heapSort(arr):
  heapify(arr)
  res = [None] * len(arr)
  for i in xrange(len(res)):
    res[i] = heappop(arr)
  return res

arr = [4,1,2,5,6,52,5,26,8,10,35,4,6,63]
print heapSort(arr)

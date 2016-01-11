'''
Bubble Sort

Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
'''


def bubbleSort(arr):
  hasSwap = True
  while hasSwap:
    hasSwap = False
    for i in xrange(0, len(arr)-1):
      j = i + 1
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        hasSwap = True

arr = [1,5,4,2,8]
bubbleSort(arr)
print arr
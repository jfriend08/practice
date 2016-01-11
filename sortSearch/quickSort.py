'''
Quick Sort
'''


def partition(arr, start, end):
  if start == end:
    return start

  idx_piviot, pVal = start, arr[start]
  arr[idx_piviot], arr[end] = arr[end], arr[idx_piviot]
  for i in xrange(start, end):
    if arr[i] <= pVal:
      arr[i], arr[idx_piviot] = arr[idx_piviot], arr[i]
      idx_piviot += 1
  arr[end], arr[idx_piviot] = arr[idx_piviot], arr[end]
  return idx_piviot

def quickSort(arr, start, end):
  if start >= end:
    return
  idx = partition(arr, start, end)
  quickSort(arr, start, idx-1)
  quickSort(arr, idx+1, end)

arr = [4,1,2,5,6,52,5,26,8,10,35,4,6,63]
quickSort(arr, 0, len(arr)-1)
print arr
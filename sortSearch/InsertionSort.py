'''
Insertion Sort
'''

def insertionSort(arr):
  sortSize = 1
  while sortSize < len(arr):
    i_replace, i_decide = sortSize, sortSize
    for i in xrange(i_replace-1, -1, -1):
      if arr[i_replace] <= arr[i]:
        i_decide = i
      else:
        break
    key, preidx = arr[i_replace], i_replace
    for i in xrange(i_replace-1, i_decide-1, -1):
      arr[i], arr[preidx] = arr[preidx], arr[i]
      preidx = i
    sortSize += 1




arr = [5,1,4,2,1,100,20,1,8]
insertionSort(arr)
print arr



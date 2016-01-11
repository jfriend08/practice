'''
K'th Smallest/Largest Element in Unsorted Array | Set 1
'''
import random as rd
def partition(arr, p_idx):
  p_val, end, idx = arr[p_idx], len(arr)-1, 0
  arr[end], arr[p_idx] = arr[p_idx], arr[end]
  for i in xrange(0, end):
    if arr[i] > arr[idx]:
      arr[i], arr[idx] = arr[idx], arr[i]
      idx += 1
  arr[end], arr[idx] = arr[idx], arr[end]
  return idx



def findKSmallestElm(arr, k):
  p_idx = rd.randint(0, len(arr)-1)
  idx = partition(arr, p_idx)
  while k != idx:
    if k > idx:
      p_idx = rd.randint(idx+1, len(arr)-1)
    elif k < idx:
      p_idx = rd.randint(0, idx - 1)

    idx = partition(arr, p_idx)
  return arr[idx]

arr = [4,1,2,5,6,52,5,26,8,10,35,4,6,63]
print findKSmallestElm(arr, 3)
# print sorted(arr)
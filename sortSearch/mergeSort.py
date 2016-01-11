'''
Merge Sort
'''

def merge(l, r):
  if len(l) == 0 or len(r) == 0:
    return (l if len(r)==0 else r)
  res = [None] * (len(l) + len(r))

  #array assignment method
  i_res, i_l, i_r = 0, 0, 0
  while i_l < len(l) and i_r < len(r):
    if l[i_l] <= r[i_r]:
      res[i_res] = l[i_l]
      i_res += 1
      i_l += 1
    elif l[i_l] > r[i_r]:
      res[i_res] = r[i_r]
      i_r += 1
      i_res += 1

  if i_l < len(l):
    for i in xrange(i_l, len(l)):
      res[i_res] = l[i]
      i_res += 1
  elif i_r < len(r):
    for i in xrange(i_r, len(r)):
      res[i_res] = r[i]
      i_res += 1

  # # bubbleSort Implementation
  # res = l + r
  # hasSwap = True
  # while hasSwap:
  #   hasSwap = False
  #   for k in xrange(0, len(res)-1):
  #     if res[k] > res[k+1]:
  #       res[k], res[k+1] = res[k+1], res[k]
  #       hasSwap = True
  return res



def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  m = len(arr)/2
  l = mergeSort(arr[:m])
  r = mergeSort(arr[m:])
  return merge(l, r)

arr = [3,1,5,2,6,4,9, 1, 1, 1, 1]
print mergeSort(arr)
'''
Convert array into Zig-Zag fashion
Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time.
The converted array should be in form a < b > c < d > e < f.

Example:
Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

Input:  arr[] =  {1, 4, 3, 2}
Output: arr[] =  {1, 4, 2, 3}
'''

import random as rd
def partition(arr,pidx):
  pval,idxLast,idxDecide = arr[pidx], len(arr)-1, 0
  arr[idxLast], arr[pidx] = arr[pidx], arr[idxLast]
  for i in xrange(len(arr)-1):
    if arr[i] <= pval:
      arr[i], arr[idxDecide] = arr[idxDecide], arr[i]
      idxDecide += 1
  arr[idxLast], arr[idxDecide] = arr[idxDecide], arr[idxLast]
  return idxDecide


#O(n) approach. Application of Quickselect
def convert2ZigZag1(arr):
  pidx, idx, seen = ((len(arr)/2) if len(arr)%2==1 else (len(arr)/2) -1), 0, {}
  print pidx, idx, seen
  while idx != pidx and not (pidx,idx) in seen:
    seen[(pidx,idx)] = True
    idx = partition(arr, pidx)

  medium = (arr[pidx] if len(arr)%2==1 else (arr[pidx]+arr[pidx+1])/2.0)
  print pidx, idx, arr, "medium -->", medium

  mid = len(arr[::2])
  arr[::2], arr[1::2] = arr[:mid][::-1], arr[mid:][::-1]
  return arr



#O(nlogn) approach
def convert2ZigZag2(arr):
  arr.sort()

  mid = len(arr[::2])
  res = [0] * len(arr)
  res[::2], res[1::2]  = arr[:mid][::-1], arr[mid:][::-1]
  return res

arr = [4,3,7,8,6,2,1]
print convert2ZigZag2(arr)

arr = [1,4,4,4,2]
# print convert2ZigZag2(arr)
convert2ZigZag1(arr)
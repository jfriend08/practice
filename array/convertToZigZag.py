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

def convert2ZigZag(arr):
  arr.sort()
  mid = len(arr[::2])
  res = [0] * len(arr)
  res[::2], res[1::2]  = arr[:mid], arr[mid:][::-1]
  return res

arr = [4,3,7,8,6,2,1]
print convert2ZigZag(arr)
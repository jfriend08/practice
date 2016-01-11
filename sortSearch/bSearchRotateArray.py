'''
Search an element in a sorted and rotated array
An element in a sorted array can be found in O(log n) time via binary search.
But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2

Algorithm:
Find the pivot point, divide the array in two sub-arrays and call binary search.
The main idea for finding pivot is: for a sorted (in increasing order) and pivoted array,
pivot element is the only only element for which next element to it is smaller than it.
'''

def findPivit(arr):
  l_i, r_i = 0, len(arr)-1
  while True:
    m_i = (l_i + r_i)/2
    if l_i > r_i:
      return -1
    elif l_i == r_i:
      return l_i
    elif arr[m_i] > arr[m_i+1]:
      return m_i
    elif arr[m_i] <= arr[l_i]:
      r_i = m_i - 1
    else:
      l_i = m_i + 1

def bSearchUtil(arr, low, high, target):
  while True:
    m = (low + high)/2
    if low > high:
      return False
    if arr[m] == target:
      return True
    elif low == high:
      return arr[low] == target
    elif target > arr[m]:
      low = m + 1
    else:
      high = m - 1

def bSearch(arr, target):
  idx = findPivit(arr)
  print idx
  if idx == -1:
    return bSearchUtil(arr, 0, len(arr)-1, target)
  else:
    if arr[0] <= target <= arr[idx]:
      return bSearchUtil(arr, 0, idx, target)
    else:
      return bSearchUtil(arr, idx+1, len(arr)-1, target)


arr = [7,8,1,2,3,4,5,6]
print bSearch(arr, 6)
arr = [3,4,5,1,1,1,1,1]
print bSearch(arr, 1)
arr = [3,4,5,6,1,2]
print bSearch(arr, 6)
arr = [1,2,3,4,5,6,7,8]
print bSearch(arr, 8)
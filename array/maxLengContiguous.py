'''
Length of the largest subarray with contiguous elements | Set 1

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5
'''
import sys
def findLeng(arr):
  maxLen = -sys.maxint-1
  for i in xrange(len(arr)-1):
    maxElm, minElm = arr[i], arr[i]
    for j in xrange(i+1, len(arr)):
      maxElm = max(maxElm, arr[j])
      minElm = min(minElm, arr[j])
      if j-i+1 == maxElm-minElm+1:
        maxLen = max(maxLen, maxElm-minElm+1)
  return maxLen

arr = [10,12,11]
print findLeng(arr)

arr = [14,12,11,20]
print findLeng(arr)

arr = [1,56,58,57,90,92,94,93,91,45]
print findLeng(arr)

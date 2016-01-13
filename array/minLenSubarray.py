'''
Minimum length subarray with sum greater than a given value

Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}
'''

import sys
def getMinLength(arr, target):
  minLen, mysum = sys.maxint, arr[0]
  left, right = 0, 0

  while right < len(arr)-1:
    if mysum > target:
      while left <= right and mysum > target:
        minLen = min(minLen, right - left + 1)
        mysum -= arr[left]
        left +=1

    elif mysum <= target:
      right += 1
      mysum += arr[right]

  return minLen

arr = [1,4,45,6,0,19]
print getMinLength(arr,51)

arr= [1, 10, 5, 2, 7]
print getMinLength(arr,9)

arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
print getMinLength(arr, 280)
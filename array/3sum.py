'''
Count triplets with sum smaller that a given value

Given an array of distinct integers and a sum value.
Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).

Examples:

Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3)

Input : arr[] = {5, 1, 3, 4, 7}
        sum = 12.
Output : 4
'''

def threeSum(arr, target):
  arr.sort()
  res = 0
  for i in xrange(len(arr)):
    for j in xrange(i+1, len(arr)):
      for k in xrange(len(arr)-1, j, -1):
        if arr[i] + arr[j] + arr[k] < target:
          res += k-j
          break
  return res


arr = [5, 1, 3, 4, 7]
print threeSum(arr, 12)

arr = [-2, 0, 1, 3]
print threeSum(arr, 2)
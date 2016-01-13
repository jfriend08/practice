'''
Partition a set into two subsets such that the difference of subset sums is minimum
Given a set of integers, the task is to divide it into two sets S1 and S2 such that
the absolute difference between their sums is minimum.

If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2
must have n-m elements and the value of abs(sum(Subset1) - sum(Subset2)) should be minimum.

Example:

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
'''
import sys
def printT(t):
  print [i for i in xrange(len(t[0]))]
  for elm in t:
    print elm

#Important. DP method to find different sums from all possible subsets
def findTable(nums):
  total = sum(nums)
  t = [ [False] * (total+1) for _ in xrange(len(nums))]

  for i in xrange(len(t)):
    t[i][0] = True
  for i in xrange(len(nums)):
    num = nums[i]
    t[i][num] = True

  for i in xrange(1,len(t)):
    for j in xrange(1,len(t[0])):
      if nums[i] == j:
        continue
      elif nums[i] > j:
        t[i][j] = t[i-1][j]
      else:
        t[i][j] = t[i-1][j-nums[i]]
  return t

def minDiffPartition(nums):
  total = sum(nums)
  table = findTable(nums)
  minDiff, bestPart = sys.maxint, None
  for j in xrange(len(table[-1])/2):
    if table[-1][j] and minDiff > total - j*2:
      minDiff = total - j*2
      bestPart = j
  return bestPart, total-bestPart


arr = [1, 6, 11, 5]
print minDiffPartition(arr)

arr = [3, 1, 4, 2, 2, 1]
print minDiffPartition(arr)
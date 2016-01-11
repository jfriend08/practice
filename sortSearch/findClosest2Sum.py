'''
Given a sorted array and a number x, find the pair in array whose sum is closest to x

Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10
'''

import sys
def findCloest2Sum(arr, target):
  diff_pre, diff_new = sys.maxint, sys.maxint
  idx, bestPair = 0, [None, None]
  while diff_new <= diff_pre and idx < len(arr):
    df_pre, df_new, localBest = sys.maxint, sys.maxint, [None, None]

    for i in xrange(len(arr)-1, idx, -1):
      df_new = abs((arr[idx]+arr[i]) - target)
      if df_new <= df_pre:
        localBest = [idx, i]
      else:
        break
      df_pre = df_new

    if df_pre <= diff_pre:
      bestPair = localBest
    else:
      break
    diff_pre = diff_new
    diff_new = df_pre
    idx += 1
    print "bestPair", bestPair, diff_pre, diff_new, df_pre, df_new

  return arr[bestPair[0]], arr[bestPair[1]]

arr = [10, 22, 28, 29, 30, 40]
print findCloest2Sum(arr, 54)

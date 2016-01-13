'''
Dynamic Programming | Set 3 (Longest Increasing Subsequence)

L[i] is the LIS which the last number ended at idx i
L[i] = 1 + max(L[j]) , j<i and arr[i] >= arr[j]

For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6
and LIS is {10, 22, 33, 50, 60, 80}.
'''

def LIS(arr):
  table = [None] * len(arr)
  table[0] = 1
  for i in xrange(1,len(arr)):
    table[i] = 1
    for j in xrange(0,i):
      if arr[j] <= arr[i] and table[i] < table[j]+1:
        table[i] = table[j]+1


  return max(table)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print LIS(arr)


'''
Dynamic Programming | Set 18 (Partition problem)
Partition problem is to determine whether a given set can be partitioned into
two subsets such that the sum of elements in both subsets is same.
'''

def partitionToSameSum(arr):
  total = sum(arr)
  if total%2 == 1:
    return False

  target = total/2
  t = [ [False] * (target+1) for _ in xrange(len(arr))]
  print "target:", target
  t[0][0], t[0][arr[0]] = True, True

  for i in xrange(1,len(arr)):
    for j in xrange(len(t[0])):
      if arr[i] < j:
        t[i][j] = t[i-1][j-arr[i]]
      elif arr[i] == j:
        t[i][j] = True
      else:
        t[i][j] = t[i-1][j]
  return sum([ t[i][-1] for i in xrange(len(arr))]) # there exist a subset that can form target

arr = [3,1,5,9,12]
print partitionToSameSum(arr)



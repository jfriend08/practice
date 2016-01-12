'''
Generate all possible sorted arrays from alternate elements of two given sorted arrays

Given two sorted arrays A and B, generate all possible arrays such that first element is
taken from A then from B then from A and so on in increasing order till the arrays exhausted.
The generated arrays should end with an element from B.

For Example
A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
'''

def findSortingAltElmsUtil(arr1, arr2, i, j, preElm, cur, res):
  if preElm == 1:
    for k in xrange(j, len(arr2)):
      if len(cur) == 0 or arr2[k] >= cur[-1]:
        findSortingAltElmsUtil(arr1, arr2, i, k, 2, cur+[arr2[k]], res)

  elif preElm == 2:
    if len(cur)!= 0: res += [cur]
    for k in xrange(i, len(arr1)):
      if len(cur) == 0 or arr1[k] >= cur[-1]:
        findSortingAltElmsUtil(arr1, arr2, k, j, 1, cur+[arr1[k]], res)


def findSortingAltElms(arr1, arr2):
  res = []
  findSortingAltElmsUtil(arr1, arr2, 0, 0, 2, [], res) #start with arr1
  return res
  # findSortingAltElmsUtil(arr1, arr2, 0, 0, 0, cur, res) #start with arr2

a = [10,15,25]
b = [1,5,20,30]
print findSortingAltElms(a, b)
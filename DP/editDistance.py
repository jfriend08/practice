'''
Dynamic Programming | Set 5 (Edit Distance)

Continuing further on dynamic programming series, edit distance is an interesting algorithm.

Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (operations) required to convert 'str1' into 'str2'.

Insert
Remove
Replace
All of the above operations are of equal cost.

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.
Replace 'n' with 'r', insert t, insert a
'''

def editDistance(str1,str2):
  t = [ [None]*(len(str2)+1) for _ in xrange(len(str1)+1)]

  for i in xrange(len(str1)+1):
    t[i][0] = i
  for j in xrange(len(str2)+1):
    t[0][j] = j

  for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):
      if str1[i-1] == str2[j-1]:
        t[i][j] = min(t[i-1][j-1], t[i-1][j]+1, t[i][j-1]+1)
      else:
        t[i][j] = min(t[i-1][j-1]+1, t[i-1][j]+1, t[i][j-1]+1)
  return t[-1][-1]

arr1 = "geek"
arr2 = "gesek"
print editDistance(arr1, arr2)

arr1 = "sunday"
arr2 = "saturday"
print editDistance(arr1, arr2)










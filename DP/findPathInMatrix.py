'''
Find the longest path in a matrix with given constraints

Given a n*n matrix where numbers all numbers are distinct and are distributed from range 1 to n2,
find the maximum length path (starting from any cell) such that all cells along the path are
increasingorder with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e.,
we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1)
with the condition that the adjacen

Example:

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9.
'''

import sys

def travel(m, i, j, maxLengMap, visited):
  dist = 1
  for delta in [[0,1], [1,0], [0,-1], [-1,0]]:
    ii, jj = i+delta[0], j+delta[1]
    if 0<=ii<len(m) and 0<=jj<len(m[0]) and not (ii,jj) in visited and m[ii][jj] == m[i][j]+1:
      visited[(ii,jj)] = True
      dist = max(dist, travel(m,ii,jj,maxLengMap,visited)+1)

  maxLengMap[(i,j)] = dist
  return dist

def findMaxLengPath(m):
  maxLengMap, maxLeng = {}, -sys.maxint-1
  for i in xrange(len(m)):
    for j in xrange(len(m[0])):
      if not (i,j) in maxLengMap:
        dist = travel(m,i,j, maxLengMap, {(i,j):True})
      else:
        dist = maxLengMap[(i,j)]
      maxLeng = max(maxLeng, dist)

  return maxLeng

m = [[1,2,9],[5,3,8],[4,6,7]]
m = [[0,0,0,0],[5,4,3,12],[6,1,2,11],[7,8,9,10]]
print findMaxLengPath(m)
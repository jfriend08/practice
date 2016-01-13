'''
Count number of ways to cover a distance
Given a distance 'dist', count total number of ways to cover the
distance with 1, 2 and 3 steps.

Examples:

Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7
'''

#Recurssion method
def numWays(dist,wayM):
  if dist < 0:
    return 0
  elif dist == 0 :
    return 1

  if dist in wayM:
    return wayM[dist]
  res = numWays(dist-1,wayM)+numWays(dist-2,wayM)+numWays(dist-3,wayM)
  wayM[dist] = res
  return res

#DP method
def numWays2(dist):
  res = [None] * (dist+1)
  if dist < 3:
    return 1 if dist == 1 else 2
  res[0], res[1], res[2] = 1, 1, 2
  for i in xrange(3,len(res)):
    res[i] = res[i-1] + res[i-2] + res[i-3]
  return res[dist]


for dist in xrange(10):
  print "dist", dist, numWays(dist,{})
print '-----------------'
for dist in xrange(10):
  print "dist", dist, numWays2(dist)
'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items
respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that
sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or
don't pick it (0-1 property).
'''

def maxValinBackpack(vals,wt,i,j,W,table):
  if i == j:
    res = (vals[i] if wt[i]<=W else 0)
  elif (i,j,W) in table:
    res = table[(i,j)]
  elif wt[i] > W:
    res = maxValinBackpack(vals,wt,i+1,j,W,table)
  else:
    res = max(vals[i]+maxValinBackpack(vals,wt,i+1,j,W-wt[i],table), maxValinBackpack(vals,wt,i+1,j,W,table) )

  table[(i,j,W)] = res
  return res

vals = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print maxValinBackpack(vals,wt,0,len(vals)-1,W,{})


vals = [10,20,5,7,32]
wt = [1,3,5,2,2]
W = 4
print maxValinBackpack(vals,wt,0,len(vals)-1,W,{})
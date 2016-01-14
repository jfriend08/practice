'''
Dynamic Programming | Set 31 (Optimal Strategy for a Game)

Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even.
We play a game against an opponent by alternating turns. In each turn, a player selects
either the first or last coin from the row, removes it from the row permanently, and
receives the value of the coin. Determine the maximum possible amount of money we can
definitely win if we move first.
'''

def winChance(vals,i,j,table):
  res = None
  if (i,j) in table:
    res = table[(i,j)]
  elif i==j:
    res = vals[i]
  elif i+1 == j:
    res = max(vals[i],vals[j])
  else:
    i_choose = vals[i] + min(winChance(vals,i+2,j,table), winChance(vals,i+1,j-1,table) )
    j_choose = vals[j] + min(winChance(vals,i,j-2,table), winChance(vals,i+1,j-1,table) )
    res = max(i_choose, j_choose)

  table[(i,j)] = res
  return res

arr = [8, 15, 3, 7]
print winChance(arr,0,len(arr)-1,{})

arr = [2, 2, 2, 2]
print winChance(arr,0,len(arr)-1,{})

arr = [20, 30, 2, 2, 2, 10]
print winChance(arr,0,len(arr)-1,{})
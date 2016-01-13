'''
Maximum difference between two elements such that larger element appears after the smaller number

Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2).
If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)
'''


def maxProfit_oneBuy(arr):
  prebuy, presell = -arr[0], 0
  buy, sell = None, None
  for i in xrange(len(arr)):
    buy = max(-arr[i], prebuy)
    sell = max(prebuy+arr[i], presell)
    prebuy, presell = buy, sell
  return sell

arr = [2,3,10,6,4,8,1]
print maxProfit_oneBuy(arr)

arr = [7,9,5,6,3,2,100]
print maxProfit_oneBuy(arr)

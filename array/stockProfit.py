'''
Stock Buy Sell to Maximize Profit

Here we are allowed to buy and sell multiple times.
'''

def maxProfit(arr):
  buy, sell = [None]*len(arr), [None]*len(arr)
  buy[0], sell[0] = -arr[0], 0

  for i in xrange(1,len(arr)):
    price = arr[i]
    buy[i] = max(buy[i-1], sell[i-1] - price)
    sell[i] = max(sell[i-1], buy[i-1] + price)
  print "buy:", buy
  print "sell:", sell
  return sell[-1]

arr = [100, 180, 260, 310, 40, 535, 695]
print maxProfit(arr)


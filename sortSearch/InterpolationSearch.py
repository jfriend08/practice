'''
Interpolation search
'''

def IerpSearch(arr, target):
  low, high = 0, len(arr)-1
  while True:
    if low > high:
      return -1

    m = low + (target - arr[low]) * ( (high-low)/(arr[high]-arr[low]) )
    if target == arr[m]:
      return m
    elif target > arr[m]:
      low = m + 1
    elif target < arr[m]:
      high = m - 1


arr = [1,2,50,500,101300,200000]
print IerpSearch(arr, 101300)

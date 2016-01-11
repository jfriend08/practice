
def findPivot(arr):
  low, high = 0, len(arr)-1
  while True:
    m = (low + high)/2

    #base case
    if low > high:
      return -1
    elif low == high:
      return low

    elif arr[m] > arr[m+1]:
      return m
    elif arr[m] < arr[low]:
      high = m - 1
    else:
      low = m + 1

def bSearchUtil(arr, low, high, target):
  while True:
    m = (low+high)/2

    if low > high:
      return -1
    elif low == high:
      return (low if target == arr[low] else -1)

    elif target == arr[m]:
      return m
    elif target > arr[m]:
      low = m + 1
    else:
      high = m - 1


def bSearch(arr, target):
  p_idx = findPivot(arr)
  if p_idx == -1:
    return bSearchUtil(arr, 0, len(arr)-1, target)
  else:
    if target == arr[p_idx]:
      return p_idx
    elif arr[0] <= target <= arr[p_idx]:
      return bSearchUtil(arr, 0, p_idx, target)
    else:
      return bSearchUtil(arr, p_idx+1, len(arr)-1, target)


arr = [3,4,5,1,1,1,1,1,1,1,2]
print bSearch(arr, 2)

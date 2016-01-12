'''
Pythagorean Triplet in an array
a^2 + b^2 = c^2

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.
'''

#based on sorted array, use two pointers
def hasStargetSum1(target, left, right, arr):
  while left < right:
    ab = arr[left]+arr[right]
    if ab == target:
      return True
    elif ab > target:
      right -= 1
    elif ab < target:
      left += 1
  return False

#use hash
def hasStargetSum2(target, left, right, arr):
  need = {}
  for i in xrange(left, right+1):
    num = arr[i]
    if num in need:
      return i, need[num]
    else:
      need[target-num] = i
  return False


def hasPythagoreanTriplet(arr):
  arr.sort()
  arr = map(lambda x: x**2, arr)
  for i in xrange(len(arr)-1, 1, -1):
    res = hasStargetSum2(arr[i], 0, i-1, arr)
    if res:
      return True
  return False



arr = [3, 1, 4, 6, 5]
print hasPythagoreanTriplet(arr)

arr = [10, 4, 6, 12, 5]
print hasPythagoreanTriplet(arr)
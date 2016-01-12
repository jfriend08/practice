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
def hasPythagoreanTriplet(arr):
  arr.sort()
  arr = map(lambda x: x**2, arr)
  for i in xrange(len(arr)-1, 1, -1):
    c, left, right = arr[i], 0, i-1
    while left < right:
      ab = arr[left]+arr[right]
      if ab == c:
        return True
      elif ab > c:
        right -= 1
      elif ab < c:
        left += 1
  return False



arr = [3, 1, 4, 6, 5]
print hasPythagoreanTriplet(arr)

arr = [10, 4, 6, 12, 5]
print hasPythagoreanTriplet(arr)
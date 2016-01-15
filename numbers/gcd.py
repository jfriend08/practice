'''
gcd, lcm
'''

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

def lcm(nums):

  '''Return lowest common multiple.'''
  def lcmUtil(a, b):
    return (a*b)/gcd(a,b)

  return reduce(lcmUtil, nums,1)

print gcd(3,5)
print gcd(3,9)
print gcd(12,18)

arr = [1,2,9]
print lcm(arr)
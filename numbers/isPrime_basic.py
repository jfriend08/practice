'''
Primality Test | Set 1 (Introduction and School Method)
isPrime basic method

We can do following optimizations:

Instead of checking till n, we can check till sqrt(n) because a larger factor of n must
be a multiple of smaller factor that has been already checked.
The algorithm can be improved further by observing that all primes are of the form 6k +- 1,
with the exception of 2 and 3. This is because all integers can be expressed as (6k + i)
for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4);
and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then
to check through all the numbers of form 6k +- 1. (Source: wikipedia)
'''

def isPrime(n):
  if n == 1:
    return False
  if n%2 == 0 or n%3 == 0:
    return False

  upBound = int(n ** 0.5) + 1
  for testNum in xrange(5, upBound, 6):
    if n%testNum == 0 or n%(testNum+1) == 0:
      return False
  return True

arr = [11,6,14,12,64,51]
print arr
print map(isPrime, arr)

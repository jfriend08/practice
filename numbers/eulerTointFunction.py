'''
Euler's Totient Function

Euler's Totient function F(n) for an input n is count of numbers in {1, 2, 3, ..., n}
that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor)
with n is 1.

Basic method: call gcd from 2 to n-1 --> complexity is O(nlogn)

Better method:
1) Initialize : result = n
2) Run a loop from 'p' = 2 to sqrt(n), do following for every 'p'.
     a) If p divides n, then
           Set: result = result  * (1.0 - (1.0 / (float) p));
           Divide all occurrences of p in n.
3) Return result
'''

def euler(n):
  result, upB = n, int(n**0.5)

  for p in xrange(2,upB):
    if n%p == 0:
      while n % p == 0:
        result *= (1.0 - (1.0/float(p)))
        print "before", n
        n /= p
        print "after", n

  return result

arr = [1,2,3,4,5,6,7,8,9,10]
print map(euler, arr)
'''
Primality Test | Set 2 (Fermat Method)

Fermat's Little Theorem:
If n is a prime number, then for every a, 1 <= a < n,

a^(n-1) = 1 (mod n)
 OR
a^(n-1) % n = 1
'''

import random as rd

def getModule(x,y,m):
  ''' return the value of (x^y)%m '''
  res, x = 1, x%m

  while y > 0:
    if y & 1: #y is odd
      res = (res*x)%m

    y = y >> 1 #y now is even
    x = (x*x)%m
  return res

def isPrime(n):
  if n <= 1 or n == 4:
    return False
  elif n<=3:
    return True

  tryC = 100
  while tryC >0:
    pickNum = 2+rd.randint(0,n-4)
    if (getModule(pickNum, n-1, n) != 1):
      return False
    tryC -= 1
  return True

arr = [11,6,14,12,64,51]
print arr
print map(isPrime, arr)





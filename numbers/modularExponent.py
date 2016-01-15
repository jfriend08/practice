'''
Modular Exponentiation (Power in Modular Arithmetic)

AB%p = ((A%p)*(B%p))%p
(x^y) % p = x%p
the term at left side is easy to get overflow, so better to do the right part instead
'''



def getModule(x,y,p):

  x, res = x%p, 1

  while y > 0:
    # if y is odd, multiply x with result
    if y & 1:
      res = (res*x)%p
    # y most be even now
    y = y>>1 #y/2
    x = (x*x)%p
  return res


print getModule(2,5,13)
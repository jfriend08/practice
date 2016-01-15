'''
Modular multiplicative inverse

The modular multiplicative inverse is an integer 'x' such that.

 a x = 1 (mod m)

The value of x should be in {0, 1, 2, ... m-1}, i.e., in the ring of integer modulo m.
'''

def modMultiplyInver(a, m):
  k = 0
  while (k*m+1)/a < m-1 and (k*m+1)%a != 0:
    k += 1

  if (k*m+1)/a < m-1:
    return (k*m+1)/a
  else:
    return -1


print modMultiplyInver(3,11)

'''
Given a string, print all possible palindromic partitions

example:
input:
        nitin
output:
        n i t i i n
        n iti n
        nitin

input:
        geeks
output:
        g e e k s
        g ee k s
'''

def isPalidrom(string):
  return "".join(string[::-1]) == string

def allPossiblePalUtil(string, start, end, collection, res):
  if start > end:
    res += [collection]
    return
  for i in xrange(start+1, len(string)+1):
    if isPalidrom(string[start:i]):
      copy = collection[:]
      allPossiblePalUtil(string, i, end, copy+["".join(string[start:i])], res)


def allPossiblePal(string):
  res = []
  allPossiblePalUtil(string, 0, len(string)-1, [], res)
  return res

string = "nitin"
print allPossiblePal(string)

string = "geeks"
print allPossiblePal(string)
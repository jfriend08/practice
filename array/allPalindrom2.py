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

def isPalindrome(string):
  return string[::-1] == string

def allPossiblePalindromeUtil(string, start, end, collection, res):
  # print string, start, end, collection, res
  if start >= end:
    res += [collection]
    return

  for i in xrange(start+1, end+1):
    if isPalindrome(string[start:i]):
      allPossiblePalindromeUtil(string, i, end, collection+[string[start:i]], res)



def allPossiblePalindrome(string):
  res = []
  allPossiblePalindromeUtil(string, 0, len(string), [], res)
  return res


string = "nitin"
print allPossiblePalindrome(string)
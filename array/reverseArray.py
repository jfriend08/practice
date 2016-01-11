'''
Reverse an array without affecting special characters

Given a string, that contains special character together with alphabets ('a' to 'z' and 'A' to 'Z'),
reverse the string in a way that special characters are not affected.
'''

import re
def reverseArrayNoAffectSpecialChar(string):
  res = [None] * len(string)
  i, j = 0, len(string)-1

  while i <= j:
    if re.match('\W', string[i]):
      res[i] = string[i]
      i += 1
    elif re.match('\W', string[j]):
      res[j] = string[j]
      j -= 1
    else:
      res[j], res[i] = string[i], string[j]
      i += 1
      j -= 1
  return "".join(res)

string = "Ab,c,de!$"
print reverseArrayNoAffectSpecialChar(string)

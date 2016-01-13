'''
Dynamic Programming | Set 4 (Longest Common Subsequence)

LCS Problem Statement: Given two sequences, find the length of longest subsequence present
in both of them. A subsequence is a sequence that appears in the same relative order, but
not necessarily contiguous.

Examples:
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.

Table to build:
  ""  A   E   D   F   H   R
""
A
E
D
F
H
R

'''

def LCS(str1, str2):
  t = [[0]*(len(str2)+1) for _ in xrange(len(str1)+1)]
  for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):
      if str1[i-1] == str2[j-1]:
        t[i][j] = t[i-1][j-1] + 1
      else:
        t[i][j] = max(t[i-1][j], t[i][j-1])
  return t[-1][-1]

str1 = "ABCDGH"
str2 = "AEDFHR"
print LCS(str1, str2)

str1 = "AGGTAB"
str2 = "GXTXAYB"
print LCS(str1, str2)

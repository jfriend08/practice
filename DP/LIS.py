'''
Dynamic Programming | Set 3 (Longest Increasing Subsequence)

L[i] is the LIS which the last number ended at idx i
L[i] = 1 + max(L[j]) , j<i and arr[i] = arr[j]
'''


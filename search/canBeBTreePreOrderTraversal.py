'''
Check if a given array can represent Preorder Traversal of Binary Search Tree

Given an array of numbers, return true if given array can represent preorder traversal
of a Binary Search Tree, else return false. Expected time complexity is O(n).

Input:  pre[] = {40, 30, 35, 80, 100}
Output: true
Given array can represent preorder traversal
of below tree
     40
   /   \
 30    80
  \      \
  35     100

Input:  pre[] = {40, 30, 35, 20, 80, 100}
Output: false
Given array cannot represent preorder traversal
of a Binary Search Tree.
'''

import sys
def canBeBTreePreOrderTransversal(nums):
  root = -sys.maxint-1 #always assume you are at right
  q = []
  for num in nums:
    if num < root:
      return False
    if len(q) != 0 and num > q[-1]:
      root = q.pop()
    q += [num]
  return True

print canBeBTreePreOrderTransversal([40, 30, 35, 20, 80, 100])
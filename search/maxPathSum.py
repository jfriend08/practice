'''
Maximum Path Sum in a Binary Tree
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

Example:

Input: Root of below tree
       1
      / \
     2   3
Output: 6
'''
import sys

class Node(object):
  def __init__(self, num):
    self.val = num
    self.left = None
    self.right = None
  def addLeft(self, node):
    self.left = node
  def addRight(self, node):
    self.right = node

class Solution(object):
  def __init__(self):
    self.maxSum = -sys.maxint-1

  def maxPathSumUtil(self, root):
    if root == None:
      return -sys.maxint-1
    if root.left == None and root.right == None:
      return root.val

    l_sum = self.maxPathSumUtil(root.left)
    r_sum = self.maxPathSumUtil(root.right)

    sum_sigle = max(root.val, root.val + max(l_sum, r_sum))
    sum_top = max(root.val, l_sum + r_sum + root.val, sum_sigle)

    self.maxSum = max(self.maxSum, sum_top)
    return sum_sigle

  def maxPathSum(self, root):
    self.maxPathSumUtil(root)
    return self.maxSum

n1, n2, n3, n4, n5, n6, n7, n8 = Node(10), Node(2), Node(10), Node(20), Node(1), Node(-25), Node(3), Node(4)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n3.addRight(n6)
n6.addLeft(n7)
n6.addRight(n8)
sol = Solution()
print sol.maxPathSum(n1)
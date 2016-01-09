'''
Find Minimum Depth of a Binary Tree
Given a binary tree, find its minimum depth. The minimum depth is the number of
nodes along the shortest path from root node down to the nearest leaf node.
'''
class Node(object):
  def __init__(self, myid):
    self.id = myid
    self.left = None
    self.right = None
  def addLeft(self, node):
    self.left = node
  def addRight(self, node):
    self.right = node

import sys
def findMinDepth(root):
  if root == None:
    return 0
  if root.left == None and root.right == None:
    return 1

  if root.left == None:
    return findMinDepth(root.right) + 1
  if root.right == None:
    return findMinDepth(root.left) + 1
  return min(findMinDepth(root.left), findMinDepth(root.right)) + 1


n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)

print findMinDepth(n1)
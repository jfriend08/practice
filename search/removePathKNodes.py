'''
Remove nodes on root to leaf paths of length < K
Given a Binary Tree and a number k, remove all nodes that lie only on root to leaf path(s) of length smaller than k.
Consider the following example Binary Tree

               1
           /      \
         2          3
      /     \         \
    4         5        6
  /                   /
 7                   8
Input: Root of above Binary Tree
       k = 4

Output: The tree should be changed to following
           1
        /     \
      2          3
     /             \
   4                 6
 /                  /
7                  8
'''

from Node import Node
def hasPathGreaterThanK(node, k):
  if node.left == None and node.right == None and k <= 1:
    return True
  elif node.left == None and node.right == None and k > 1:
    return False

  left_r, right_r = False, False
  if node.left != None:
    left_r = hasPathGreaterThanK(node.left, k-1)
    if not left_r:
      node.left = None
  if node.right != None:
    right_r = hasPathGreaterThanK(node.right, k-1)
    if not right_r:
      node.right = None
  return left_r or right_r

def removeNodePathSmallerThanK(node, k):
  if node != None and k < 1:
    return node

  hasPathGreaterThanK(node, k)
  return node

def printTree(node):
  level, q, res = 0, [[0,node]], {}
  while len(q) != 0:
    level, node = q.pop(0)
    if level in res:
      res[level] += [node.val]
    else:
      res[level] = [node.val]
    if node.left != None:
      q += [[level+1,node.left]]
    if node.right != None:
      q += [[level+1, node.right]]
  return [res[k] for k in sorted(res.keys())]


n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n4.addLeft(n7)
n3.addRight(n6)
n6.addLeft(n8)
print printTree(n1)
print printTree(removeNodePathSmallerThanK(n1, 4))


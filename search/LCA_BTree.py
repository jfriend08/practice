'''
Lowest Common Ancestor in a Binary Search Tree.
Given values of two nodes in a Binary Search Tree, write a c program to
find the Lowest Common Ancestor (LCA). You may assume that both the values exist in the tree.

              20
           /      \
         8          22
      /     \
    4         12
             /   \
            10    14
Input: Root of above Binary Tree, node 10 and node 14
Output: 12
'''
from Node import Node
def findLCA(root, n1, n2):
  if root.val > n1.val and root.val > n2.val and root.left != None:
    return findLCA(root.left, n1, n2)
  elif root.val < n1.val and root.val < n2.val and root.right != None:
    return findLCA(root.right, n1, n2)
  else:
    return root.val



n1, n2, n3, n4, n5, n6, n7 = Node(20), Node(8), Node(22), Node(4), Node(12), Node(10), Node(14)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n5.addLeft(n6)
n5.addRight(n7)

print findLCA(n1, n6, n4)


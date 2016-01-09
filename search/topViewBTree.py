'''
Print Nodes in Top View of Binary Tree
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
Top view of the above binary tree is
4 2 1 3 7
'''

from Node import Node
def topViewBTreeUtil(node, posM, pos):
  if node.left != None:
    topViewBTreeUtil(node.left, posM, pos-1)
  if node.right != None:
    topViewBTreeUtil(node.right, posM, pos+1)

  #update in post-oreder fashion
  posM[pos] = node.val

def topViewBTree(node):
  if node == None:
    return
  posM = {}
  topViewBTreeUtil(node, posM, 0)
  return [posM[key] for key in sorted(posM.keys())]

n1, n2, n3, n4, n5, n6, n7, n8 = Node(20), Node(8), Node(22), Node(5), Node(3), Node(25), Node(10), Node(14)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n3.addRight(n6)
n5.addLeft(n7)
n5.addRight(n8)
print topViewBTree(n1)




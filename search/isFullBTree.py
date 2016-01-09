'''
Check whether a binary tree is a full binary tree or not
A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes.
Conversely, there is no node in a full binary tree, which has one child node. More information about full binary trees can be found here.
'''
from Node import Node
def isFullBTree(root):
  if root == None:
    return False
  if root.left == None and root.right == None:
    return True

  myQ = [root]
  while len(myQ) != 0:
    node = myQ.pop(0)
    if node.left == None and node.right == None:
      continue
    elif node.left != None and node.right != None:
      myQ += [node.left, node.right]
    else:
      return False
  return True


n1, n2, n3, n4, n5, n6, n7, n8, n9 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n3.addLeft(n6)
n3.addRight(n7)
n7.addLeft(n8)
# n7.addRight(n9)
print isFullBTree(n1)
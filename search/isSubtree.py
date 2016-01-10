'''
Check if a binary tree is subtree of another binary tree | Set 2
Given two binary trees, check if the first tree is subtree of the second one.
A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.

For example, in the following case, Tree1 is a subtree of Tree2.


        Tree1
          x
        /    \
      a       b
       \
        c


        Tree2
              z
            /   \
          x      e
        /    \     \
      a       b      k
       \
        c
'''

from Node import Node
def inOrderT(node):
  if node == None:
    return []
  res = []
  if node.left != None:
    res += inOrderT(node.left)
  res += [node.val]
  if node.right != None:
    res += inOrderT(node.right)
  return res

def preOrderT(node):
  if node == None:
    return []
  res = [node.val]
  if node.left != None:
    res += preOrderT(node.left)
  if node.right != None:
    res += preOrderT(node.left)
  return res

def isSubtree(node1, node2):
  node1_in, node1_pre = set(inOrderT(node1)), set(preOrderT(node1))
  node2_in, node2_pre = set(inOrderT(node2)), set(preOrderT(node2))

  return node1_in.issubset(node2_in) and node1_pre.issubset(node2_pre)

n1, n2, n3, n4 = Node("x"), Node("a"), Node("b"), Node("c")
n1.addLeft(n2)
n1.addRight(n3)
n2.addRight(n4)
N1, N2, N3, N4, N5, N6, N7 = Node("z"), Node("x"), Node("e"), Node("a"), Node("b"), Node("k"), Node("c")
N1.addLeft(N2)
N1.addRight(N3)
N2.addLeft(N4)
N2.addRight(N5)
N3.addRight(N6)
N4.addRight(N7)

print isSubtree(n1, N1)
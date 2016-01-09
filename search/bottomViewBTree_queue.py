'''
Bottom View of a Binary Tree -- Queue Implementation
Given a Binary Tree, we need to print the bottom view from left to right.

Examples:

                      20
                    /    \
                  8       22
                /   \      \
              5      3      25
                    / \
                  10    14

For the above tree the output should be 5, 10, 3, 14, 25.
'''

from Node import Node

def bottomView(root):
  if root == None:
    return

  posM, pos, q = {}, 0, [[0, root]]

  while len(q) > 0:
    pos, node = q.pop(0)
    posM[pos] = node.val
    if node.left != None:
      q += [[pos-1, node.left]]
    if node.right != None:
      q += [[pos+1, node.right]]
  res = []
  for pos in sorted(posM.keys()):
    res += [posM[pos]]
  return res

n1, n2, n3, n4, n5, n6, n7, n8 = Node(20), Node(8), Node(22), Node(5), Node(3), Node(25), Node(10), Node(14)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n3.addRight(n6)
n5.addLeft(n7)
n5.addRight(n8)
print bottomView(n1)




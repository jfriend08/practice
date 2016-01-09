'''
Bottom View of a Binary Tree
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
def update(root, left, right, pos):
  if pos <= 0:
    try:
      left[-pos] += [root.val]
    except:
      left += [[root.val]]
  else:
    try:
      right[pos-1] += [root.val]
    except:
      right += [[root.val]]

def bottomViewUtil(root, left, right, pos):
  update(root, left, right, pos)
  if root.left != None:
    bottomViewUtil(root.left, left, right, pos-1)

  if root.right != None:
    bottomViewUtil(root.right, left, right, pos+1)

def bottomView(root):
  if root == None:
    return
  left, right = [], []
  bottomViewUtil(root, left, right, 0)
  return [elm[-1] for elm in left[::-1]] + [elm[0] for elm in right]

n1, n2, n3, n4, n5, n6, n7, n8 = Node(20), Node(8), Node(22), Node(5), Node(3), Node(25), Node(10), Node(14)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n3.addRight(n6)
n5.addLeft(n7)
n5.addRight(n8)
print bottomView(n1)
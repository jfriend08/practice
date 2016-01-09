'''
Reverse alternate levels of a full binary tree
Given a Full Binary Tree, reverse the alternate level nodes of the binary tree.
Given tree:
               a
            /     \
           b       c
         /  \     /  \
        d    e    f    g
       / \  / \  / \  / \
       h  i j  k l  m  n  o

Modified tree:
               a
            /     \
           c       b
         /  \     /  \
        d    e    f    g
       / \  / \  / \  / \
      o  n m  l k  j  i  h
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


class Solution(object):
  def __init__(self):
    self.map = {}
    self.nodeAtLevels = []

  def travel(self, root, level):
    if level % 2 == 1:
      try:
        self.map[level] += [root.id]
      except:
        self.map[level] = [root.id]

    if root.left != None:
      self.travel(root.left, level+1)
    if root.right != None:
      self.travel(root.right, level+1)
    return

  def travelUpdate(self, root, level):
    if level % 2 == 1:
      root.id = self.map[level].pop()
    if root.left != None:
      self.travelUpdate(root.left, level+1)
    if root.right != None:
      self.travelUpdate(root.right, level+1)
    return

  def printNode(self, root, level):
    try:
      self.nodeAtLevels[level] += [root.id]
    except:
      self.nodeAtLevels += [[root.id]]
    if root.left != None:
      self.printNode(root.left, level+1)
    if root.right != None:
      self.printNode(root.right, level+1)

  def reverseAltLevels(self, root):
    if root == None:
      return
    self.travel(root, 0)
    self.travelUpdate(root, 0)
    self.printNode(root, 0)
    print self.nodeAtLevels

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11), Node(12), Node(13), Node(14), Node(15)
n1.addLeft(n2)
n1.addRight(n3)
n2.addLeft(n4)
n2.addRight(n5)
n3.addLeft(n6)
n3.addRight(n7)
n4.addLeft(n8)
n4.addRight(n9)
n5.addLeft(n10)
n5.addRight(n11)
n6.addLeft(n12)
n6.addRight(n13)
n7.addLeft(n14)
n7.addRight(n15)
sol = Solution()

sol.reverseAltLevels(n1)









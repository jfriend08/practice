

class Node(object):
  def __init__(self, num):
    self.val = num
    self.left = None
    self.right = None
  def addLeft(self, node):
    self.left = node
  def addRight(self, node):
    self.right = node
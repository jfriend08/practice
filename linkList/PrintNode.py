def printNode(node):
  while node != None and node.next != None:
    print node.val
    node = node.next
  print node.val
def printNode(node):
  if node == None:
    print None
    return
  while node != None and node.next != None:
    print node.val
    node = node.next
  print node.val
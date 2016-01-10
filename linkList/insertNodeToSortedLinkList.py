'''
Given a linked list which is sorted, how will you insert in sorted way
1) If Linked list is empty then make the node as head and return it.
2) If value of the node to be inserted is smaller than value of head node
    then insert the node at start and make it head.
3) In a loop, find the appropriate node after which the input node (let 9) is
    to be inserted. To find the appropriate node start from head, keep moving
    until you reach a node GN (10 in the below diagram) who's value is
    greater than the input node. The node just before GN is the appropriate
    node (7).
4) Insert the node (9) after the appropriate node (7) found in step 3.
'''
from ListNode import ListNode
def printNode(node):
  while node != None and node.next != None:
    print node.val
    node = node.next
  print node.val
def insertNode(head, node):
  if head == None:
    return node
  if node.val < head.val:
    node.next = head
    return node

  fastp, slowp = head.next, head
  while fastp != None and fastp.next != None:
    if fastp.val > node.val:
      slowp.next = node
      node.next = fastp
      return head
    else:
      slowp = fastp
      fastp = fastp.next

  fastp.next = node
  return head

n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(5), ListNode(10), ListNode(11)
node = ListNode(100)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
printNode(insertNode(n1, node))


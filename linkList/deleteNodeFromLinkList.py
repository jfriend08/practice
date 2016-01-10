'''
Delete a given node in Linked List under given constraints
'''
import PrintNode as pn
from ListNode import ListNode
def deleteNode(head, node):
  if head == None:
    return
  if node.val == head.val:
    return head.next

  fast, slow = head.next, head
  while fast != None and fast.next != None:
    if fast.val == node.val:
      slow.next = fast.next
      return head
    else:
      slow = fast
      fast = fast.next
  if fast.val == node.val:
    slow.next = None

  return head

n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(5), ListNode(10), ListNode(11)
node = ListNode(100)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
pn.printNode(deleteNode(n1, node))



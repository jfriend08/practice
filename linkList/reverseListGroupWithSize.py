'''
Reverse a Linked List in groups of given size
Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.

Inputs:  1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.
'''

import PrintNode as pn
from ListNode import ListNode

def reverseListRecur(head, k):
  if k > 1:
    newTail, newHead = reverseListRecur(head.next, k-1)
    newTail.next = head
    return (head, newHead)
  else:
    return (head, head)

def reverseList(head, k):
  head_lastPart, count = head, 1
  while head_lastPart != None and count <= k:
    head_lastPart = head_lastPart.next
    count += 1

  if head_lastPart == None and count < k:
    return #k longer than the list. simply not possible

  newTail, newHead = reverseListRecur(head, k)
  newTail.next = head_lastPart

  return newHead

N1, N2, N3, N4, N5, N6, N7, N8 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6), ListNode(7), ListNode(8)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
N5.next = N6
N6.next = N7
N7.next = N8

pn.printNode(reverseList(N1, 8))
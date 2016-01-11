'''
Detect and Remove Loop in a Linked List
Write a function detectAndRemoveLoop() that checks whether a given Linked List contains loop and if loop
is present then removes the loop and returns true. And if the list doesn't contain loop then returns false.

Below diagram shows a linked list with a loop. detectAndRemoveLoop() must change the below list to 1->2->3->4->5->NULL.
'''

import PrintNode as pn
from ListNode import ListNode

def detectAndRemoveLoop(head):
  fast, slow = head, head
  while fast.next.next != slow:
    fast = fast.next.next
    slow = slow.next
  slow = slow.next

  p, numNodes = slow.next, 1
  while p != slow:
    p = p.next
    numNodes += 1

  count, p1 = 0, head
  while count != numNodes:
    p1 = p1.next
    count += 1

  p1_slow, p2 = p1, head
  while p2 != p1:
    p1_slow = p1
    p1 = p1.next
    p2 = p2.next


  p1_slow.next = None
  return head


N1, N2, N3, N4, N5, N6, N7, N8, N9, N10 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6), ListNode(7), ListNode(8), ListNode(9), ListNode(10)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
N5.next = N6
N6.next = N7
N7.next = N8
N8.next = N9
N9.next = N10
N10.next = N4

pn.printNode(detectAndRemoveLoop(N1))

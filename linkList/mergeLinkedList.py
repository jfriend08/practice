'''
Merge a linked list into another linked list at alternate positions
list1: 5->7->17->13->11
list2: 12->10->2->4->6
Results:
list1: 5->12->7->10->17->2->13->4->11->6
list2: empty

list1: 1->2->3
list2: 4->5->6->7->8
Results:
list1: 1->4->2->5->3->6
list2: 7->8.
'''

import PrintNode as pn
from ListNode import ListNode

def mergeLinkedList(h1, h2):
  p1, p2 = h1, h2
  while p1 != None and p2 != None:
    tmp = p1.next
    p1.next = p2
    p2 = p2.next
    p1.next.next = tmp
    p1 = tmp
  return h1, p2


n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
n1.next = n2
n2.next = n3

N1, N2, N3, N4, N5 = ListNode(4), ListNode(5), ListNode(6), ListNode(7), ListNode(8)
N1.next = N2
N2.next = N3
# N3.next = N4
# N4.next = N5

r1, r2 = mergeLinkedList(n1, N1)
pn.printNode(r1)
print "--------------------"
pn.printNode(r2)
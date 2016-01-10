'''
Union and Intersection of two Linked Lists
Given two Linked Lists, create union and intersection lists that contain union and intersection
of the elements present in the given lists. Order of elments in output lists doesn't matter.

Example:

Input:
   List1: 10->15->4->20
   lsit2: 8->4->2->10
Output:
   Intersection List: 4->10
   Union List: 2->8->20->4->15->10
'''

import PrintNode as pn
from ListNode import ListNode

def merge(p1, p2):
  if not p1 or not p2:
    return p1 or p2

  newHead = ListNode(None)
  newHead_p = newHead
  while p1 != None and p2 != None:
    if p1.val <= p2.val:
      newHead_p.next = p1
      p1 = p1.next
    else:
      newHead_p.next = p2
      p2 = p2.next
    newHead_p = newHead_p.next
  newHead_p.next = (p1 if p1 != None else p2)
  return newHead.next

def mergeSort(head):

  if head == None or head.next == None:
    return head

  fast, slow = head, head

  while fast.next != None and fast.next.next != None:
    fast = fast.next.next
    slow = slow.next

  l,r,slow.next = head, slow.next, None
  l = mergeSort(l)
  r = mergeSort(r)
  return merge(l, r)

def unionAndIntersection(head1, head2):
  h_interset, h_union = ListNode(None), ListNode(None)
  interset_p, union_p = h_interset, h_union
  head1, head2 = mergeSort(head1), mergeSort(head2)
  while head1 != None and head2 != None:
    if head1.val < head2.val:
      interset_p.next = head1
      head1 = head1.next
      interset_p = interset_p.next
    elif head1.val > head2.val:
      interset_p.next = head2
      head2 = head2.next
      interset_p = interset_p.next
    else:
      union_p.next = head1
      while head1 != None and head1.val == union_p.next.val:
        head1 = head1.next
      while head2 != None and head2.val == union_p.next.val:
        head2 = head2.next
      union_p = union_p.next

  interset_p.next = (head1 if head1 != None else head2)

  return h_interset.next, h_union.next



n1, n2, n3, n4, n5, n6 = ListNode(2), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(10)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

N1, N2, N3, N4, N5, N6, N7, N8 = ListNode(10), ListNode(2), ListNode(31), ListNode(14), ListNode(21), ListNode(53), ListNode(11), ListNode(13)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
N5.next = N6
N6.next = N7
N7.next = N8


pn.printNode(n1)
print '----------------------'
pn.printNode(N1)
print '----------------------'

interset, union = unionAndIntersection(n1, N1)
pn.printNode(interset)
print '----------------------'
pn.printNode(union)




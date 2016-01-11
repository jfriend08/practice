'''
Merge Sort for Linked Lists
'''

import PrintNode as pn
from ListNode import ListNode

def merge(l, r):
  if not l or not r:
    return l or r

  head = ListNode(None)
  hp = head

  while l != None and r != None:
    if l.val <= r.val:
      hp.next = l
      l = l.next
    elif r.val <= l.val:
      hp.next = r
      r = r.next
    hp = hp.next

  hp.next = (l if l != None else r)
  return head.next

def mergeSort(head):
  if head == None or head.next == None:
    return head

  fast, slow = head, head
  while fast.next != None and fast.next.next != None:
    fast = fast.next.next
    slow = slow.next
  l, r, slow.next = head, slow.next, None
  l = mergeSort(l)
  r = mergeSort(r)
  return merge(l, r)



N1, N2, N3, N4, N5, N6, N7, N8, N9, N10 = ListNode(11), ListNode(2), ListNode(31), ListNode(14), ListNode(25), ListNode(64), ListNode(7), ListNode(18), ListNode(49), ListNode(15)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
N5.next = N6
N6.next = N7
N7.next = N8
N8.next = N9
N9.next = N10

pn.printNode(N1)
print '----------------------'
pn.printNode(mergeSort(N1))
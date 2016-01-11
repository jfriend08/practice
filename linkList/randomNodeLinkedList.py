'''
Select a Random Node from a Singly Linked List
'''

import random as rd
import PrintNode as pn
from ListNode import ListNode

def getRandomNode(head):
  res, n, p = head, 1, head
  while p != None:
    if rd.randint(0, n) == 0:
      res = p
    p = p.next
    n += 1

  return res

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

c = 0
while c != 100:
  res = getRandomNode(N1)
  print res.val
  c += 1


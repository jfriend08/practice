'''
Compare two strings represented as linked lists
Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s->b
Output: -1

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s
Output: 1

Input: list1 = g->e->e->k->s
       list2 = g->e->e->k->s
Output: 0
'''
from ListNode import ListNode
def compareString(h1, h2):
  p1, p2 = h1, h2

  if p1 == None or p2 == None:
    return -1

  while p1 != None and p2 != None:
    if p1.val != p2.val:
      return -1
    p1 = p1.next
    p2 = p2.next

  return (0 if p1==None and p2==None else 1)

n1, n2, n3, n4, n5, n6 = ListNode("g"), ListNode("e"), ListNode("e"), ListNode("k"), ListNode("s"), ListNode("a")
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

N1, N2, N3, N4, N5, N6 = ListNode("g"), ListNode("e"), ListNode("e"), ListNode("k"), ListNode("s"), ListNode("b")
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
# N5.next = N6

print compareString(n1, N1)
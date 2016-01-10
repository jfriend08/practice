'''
Add two numbers represented by linked lists | Set 2

Given two numbers represented by two linked lists, write a function that returns sum list.
The sum list is linked list representation of addition of two input numbers. It is not allowed
to modify the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).
'''
import PrintNode as pn
from ListNode import ListNode

def addNumEvenLeng(n1, n2, n1isLonger):
  if n1.next != None and n2.next != None:
    needToAdd1 = addNumEvenLeng(n1.next, n2.next, n1isLonger)
    val = (n1.val + n2.val + 1 if needToAdd1 else n1.val + n2.val)
    if n1isLonger:
      n1.val = val%10
    else:
      n2.val = val%10
    return val>=10
  else:
    val = n1.val + n2.val
    if n1isLonger:
      n1.val = val%10
    else:
      n2.val = val%10
    return val >= 10

def addNumRecur(n1, n2, n1isLonger, diff):
  if n1isLonger and diff > 0:
    needToAdd1 = addNumRecur(n1.next, n2, n1isLonger, diff-1)
    if needToAdd1:
      val = n1.val + 1
      n1.val = val%10
      return val >=10
  elif not n1isLonger and diff > 0:
    needToAdd1 = addNumRecur(n1, n2.next, n1isLonger, diff-1)
    if needToAdd1:
      val = n2.val + 1
      n2.val = val%10
      return val >=10
  else:
    return addNumEvenLeng(n1, n2, n1isLonger)

def getLeng(node):
  count = 0
  while node != None:
    count += 1
    node = node.next
  return count

def addNumbers(h1, h2):
  l1, l2 = getLeng(h1), getLeng(h2)
  needToAdd1 = addNumRecur(h1, h2, l1 >= l2, abs(l1-l2))
  if needToAdd1:
    newN = ListNode(1)
    newN.next = (h1 if l1>=l2 else h2)
    return newN
  else:
    return (h1 if l1>=l2 else h2)

n1, n2, n3 = ListNode(5), ListNode(6), ListNode(3)
n1.next = n2
n2.next = n3

N1, N2, N3, N4 = ListNode(8), ListNode(4), ListNode(2), ListNode(2)
N1.next = N2
N2.next = N3
# N3.next = N4
pn.printNode(addNumbers(n1, N1))





'''
Add two numbers represented by linked lists | Set 2

Given two numbers represented by two linked lists, write a function that returns sum list.
The sum list is linked list representation of addition of two input numbers. It is not allowed
to modify the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).
'''
import PrintNode as pn
from ListNode import ListNode
def addNumRecur(n1, n2, n1Leng, n2Leng):
  if n1.next == None and n2.next != None:
    needAddOne, isn1Longer = addNumRecur(n1, n2.next, n1Leng, n2Leng+1)
    if needAddOne:
      val = n2.val + 1
      n2.val = val%10
      return (val>=10, isn1Longer)
    else:
      return (n2.val>=10, isn1Longer)

  elif n1.next != None and n2.next == None:
    needAddOne, isn1Longer = addNumRecur(n1.next, n2, n1Leng+1, n2Leng)
    if needAddOne:
      val = n1.val + 1
      n1.val = val%10
      return (val>=10, isn1Longer)

  elif n1.next != None and n2.next != None:
    needAddOne, isn1Longer = addNumRecur(n1.next, n2.next, n1Leng+1, n2Leng+1)
    if isn1Longer and needAddOne:
      val = n1.val + 1
      n1.val = val%10
      return (val>=10, isn1Longer)
    elif not isn1Longer and needAddOne:
      val = n2.val + 1
      n2.val = val%10
      return (val>=10, isn1Longer)
    else:
      return (False, isn1Longer)

  else:
    if n1Leng >= n2Leng:
      n1.val = (n1.val+n2.val)%10
    else:
      n2.val = (n1.val+n2.val)%10
    return (n1.val+n2.val >=10, n1Leng >= n2Leng)

def addNumbers(h1, h2):
  if h1 == None and h2 == None:
    return
  elif h1 == None:
    return h2
  elif h2 == None:
    return h1
  else:
    (needAddOne, isn1Longer) = addNumRecur(h1, h2, 1, 1)
    if needAddOne:
      newh = LinkNode(1)
      newh.next = (h1 if isn1Longer else h2)
      return newh
    else:
      return (h1 if isn1Longer else h2)


n1, n2, n3 = ListNode(5), ListNode(6), ListNode(3)
n1.next = n2
n2.next = n3

N1, N2, N3 = ListNode(8), ListNode(4), ListNode(2)
N1.next = N2
N2.next = N3

pn.printNode(addNumbers(n1, N1))





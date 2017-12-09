"""
Merge two linked list
head could be None as well for empty list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
   self.data = data
   self.next = next_node

return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    same = True
    while headA is not None and headB is not None:
        if headA.data != headB.data:
            same = False
        headA = headA.next
        headB = headB.next

    if same is False or headA != headB:
        return 0
    else:
        return 1

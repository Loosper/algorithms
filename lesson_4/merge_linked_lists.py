"""
Merge two linked lists
head could be None as well for empty list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
   self.data = data
   self.next = next_node

return back the head of the linked list in the below method.
"""


def MergeLists(headA, headB):
    first = result = Node()

    while headA is not None and headB is not None:
        if headA.data < headB.data:
            nxt = headA
            headA = headA.next
        else:
            nxt = headB
            headB = headB.next

        result.next = nxt
        result = result.next

    result.next = headB if headA is None else headA
    return first.next

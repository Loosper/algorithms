"""
Reverse a linked list
head could be None as well for empty list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
   self.data = data
   self.next = next_node

return back the head of the linked list in the below method.
"""


class Node:
    pass


def Reverse(head):
    if head is None:
        return None

    legit_head = head
    prev = None

    while True:
        next = head.next
        if head.next is not None:
            head.next = prev
            prev = head
            head = next
        else:
            head.next = prev
            legit_head = head
            break

    return legit_head

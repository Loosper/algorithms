"""
Delete Node at a given position in a linked list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
   self.data = data
   self.next = next_node

return back the head of the linked list in the below method.
"""


class Node:
    pass


def Delete(head, position):
    legit_head = head

    for i in range(position - 1):
        head = head.next

    if position == 0:
        legit_head = legit_head.next
    else:
        head.next = head.next.next

    return legit_head

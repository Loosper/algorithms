"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


class Node:
    pass


def InsertNth(head, data, position):
    legit_head = head

    for i in range(position - 1):
        head = head.next

    if position == 0:
        legit_head = Node(data, legit_head)
    else:
        next = head.next
        head.next = Node(data, next)

    return legit_head

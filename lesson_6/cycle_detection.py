"""
Detect a cycle in a linked list. Note that the head pointer may be 'None'
if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    slow = head
    fast = head.next
    while True:
        if slow is None or fast is None:
            return False
        if slow == fast:
            return True

        # this could blow up due to None, however it passes
        slow = slow.next
        fast = fast.next.next

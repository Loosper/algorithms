"""
Find the node at which both lists merge and return the data of that node.
head could be None as well for empty list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
   self.data = data
   self.next = next_node


"""


def get_length(head):
    count = 0
    while head.next is not None:
        count += 1
        head = head.next

    return count


def FindMergeNode(headA, headB):
    lenA = get_length(headA)
    lenB = get_length(headB)

    for _ in range(abs(lenA - lenB)):
        if lenA > lenB:
            headA = headA.next
        else:
            headB = headB.next

    while headA is not None:
        if headA is headB:
            return headA.data

        headA = headA.next
        headB = headB.next

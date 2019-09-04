"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
# """


def flat(head):
    # print(head.val)
    head1 = head
    prev = None
    while (head1):
        if head1.child:
            # print(head1.val)
            ctail = flat(head1.child)
            temp = None
            if head1.next:
                temp = head1.next
                temp.prev = ctail
                ctail.next = temp
            head1.next = head1.child
            head1.child.prev = head1
            head1.child = None

            head1 = temp
            if head1:
                prev = head1.prev
            else:
                prev = ctail

        else:
            prev = head1
            head1 = head1.next

    return prev


class Solution(object):
    def flatten(self, head):
        head1 = head
        flat(head1)

        return head

        """
        :type head: Node
        :rtype: Node
        """

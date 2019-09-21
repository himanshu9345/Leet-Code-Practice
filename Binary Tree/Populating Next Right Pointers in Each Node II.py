"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


def conn2(root):  # not working
    curr = root
    next = root.left

    while curr.left:
        if curr.next:
            if curr.left:
                if curr.right:
                    curr.left.next = curr.right
                elif curr.next:
                    if curr.next.left:
                        curr.left.next = curr.next.left
                    else:
                        curr.left.next = curr.next.right
                curr = curr.next
            elif curr.right:
                if curr.next:
                    if curr.next.left:
                        curr.right.next = curr.next.left
                    else:
                        curr.right.next = curr.next.right
                curr = curr.next
        else:
            curr = next
            if next.left:
                next = next.left
            elif next.right:
                next = next.right
            else:
                next = next.next
    return root


def conn(root):  # working
    queue = [root]

    while queue:
        new1 = []
        for i in range(len(queue)):
            if queue[i].left:
                new1.append(queue[i].left)
            if queue[i].right:
                new1.append(queue[i].right)
            if i <= len(queue) - 2:
                # print(queue[i].val)
                queue[i].next = queue[i + 1]
            else:
                queue[i].next = None
        queue = new1
    return root


class Solution(object):
    def connect(self, root):
        if root:
            return conn2(root)
        else:
            return None
        """
        :type root: Node
        :rtype: Node
        """

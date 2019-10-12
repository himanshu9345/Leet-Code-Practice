"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


def conn(root):
    queue = [root]

    while queue:
        new1 = []
        for i in range(len(queue)):
            if queue[i].left:
                new1.append(queue[i].left)
            if queue[i].right:
                new1.append(queue[i].right)
            if i <= len(queue) - 2:
                print(queue[i].val)
                queue[i].next = queue[i + 1]
            else:
                queue[i].next = None
        queue = new1
    return root


class Solution(object):
    def connect(self, root):
        if root:
            return conn(root)
        else:
            return None
        # return root

        """
        :type root: Node
        :rtype: Node
        """

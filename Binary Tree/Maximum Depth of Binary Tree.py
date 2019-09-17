# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    ans = 0

    def postorder(self, root):
        if not root:
            return 0
        return max(self.postorder(root.left), self.postorder(root.right)) + 1

    def preorder(self, root, depth):
        if root:
            if not root.left and not root.right:
                self.ans = max(depth, self.ans)
            self.preorder(root.left, depth + 1)
            self.preorder(root.right, depth + 1)
        return

    def maxDepth(self, root):

        return self.postorder(root)
        # return self.ans
        """
        :type root: TreeNode
        :rtype: int
        """

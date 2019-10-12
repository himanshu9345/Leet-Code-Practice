# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            el = stack.pop()
            if el:
                ans.append(el.val)
                stack.append(el.left)
                stack.append(el.right)
        return ans[::-1]

        """
        :type root: TreeNode
        :rtype: List[int]
        """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        """
        :type root: TreeNode  
        :rtype: List[int]
        """

    def preorderTraversal1(self, root):
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            el = stack.pop()
            if el:
                ans.append(el.val)
                stack.append(el.right)
                stack.append(el.left)
        return ans
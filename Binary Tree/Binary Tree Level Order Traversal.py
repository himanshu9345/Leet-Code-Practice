# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            new1 = []
            ans1 = []
            for i in queue:
                ans1.append(i.val)
                if i.left:
                    new1.append(i.left)
                if i.right:
                    new1.append(i.right)
            queue = new1
            ans.append(ans1)
        return ans
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

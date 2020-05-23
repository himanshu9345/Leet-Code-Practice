# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root1):
        if not root1:
            return None
        queue = collections.deque([root1])
        nextlevel = collections.deque()
        ans = []
        while queue:
            root = queue.popleft()
            if root.left:
                nextlevel.append(root.left)
            if root.right:
                nextlevel.append(root.right)
            
            if not queue:
                ans.append(root.val)
                queue, nextlevel = nextlevel,queue
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
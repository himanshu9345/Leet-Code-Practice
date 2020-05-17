# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorder(self,root, max_yet):
        if not root:
            return 0
        max_yet = max(max_yet, root.val)
        count = 0
        if root.left and max_yet <= root.left.val:
            count += 1
        if root.right and max_yet <= root.right.val:
            count += 1
        
        count += self.inorder(root.left, max_yet)
        count += self.inorder(root.right,max_yet)
        
        return count
    
    def goodNodes(self, root):
        if root:
            return self.inorder(root, root.val) + 1
        """
        :type root: TreeNode
        :rtype: int
        """
        
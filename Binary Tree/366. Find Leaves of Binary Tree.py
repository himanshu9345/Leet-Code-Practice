# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self, root, depth, dict1):
        if root:
            if root.left:
                self.postorder(root.left, depth+1, dict1)
            if root.right:
                self.postorder(root.right, depth+1, dict1)
            
            dict1[depth].append(root.val)
        return
    def findLeaves(self, root):
        if not root:
            return []
        dict1 = collections.defaultdict(list)
        self.postorder(root, 0, dict1)
        ans = []
        for i in sorted(dict1, reverse = True):
            ans.append(dict1[i])
        print ans
        
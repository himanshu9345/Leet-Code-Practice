# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preorder(root, sum1):
    if not root:
        if sum1 == 0:
            return True
        else:
            return False
    res = False
    if sum1 - root.val == 0 and not root.right and not root.left:
        res = True
    # print res,sum1
    if root.left:
        res = res or preorder(root.left, sum1 - root.val)
    if root.right:
        res = res or preorder(root.right, sum1 - root.val)
    return res


class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        return preorder(root, sum)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

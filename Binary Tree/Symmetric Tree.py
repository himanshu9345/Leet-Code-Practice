# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def postorder(root, sum1, str1, argv):
    if not root:
        # print str1
        return str1
    # print str1
    str11 = ""
    str2 = ""
    if argv == 0:
        str11 = postorder(root.left, sum1 + 1, str1 + "#", 1)
        str2 = postorder(root.right, sum1 + 1, str1 + "#", 2)
    if argv == 1:
        str11 = postorder(root.left, sum1 + 1, str1 + "#", 1)
        str2 = postorder(root.right, sum1 + 1, str1 + "#", 1)
    if argv == 2:
        str11 = postorder(root.right, sum1 + 1, str1 + "#", 2)
        str2 = postorder(root.left, sum1 + 1, str1 + "#", 2)
    if sum1 == 1:
        # print str11,str2
        return str11 == str2
    return str11 + str(root.val) + str2


def check(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val) and check(left.left, right.right) and check(left.right, right.left)


class Solution(object):
    def isSymmetric(self, root):
        return check(root, root)
        """
        :type root: TreeNode
        :rtype: bool
        """

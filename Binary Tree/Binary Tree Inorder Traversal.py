# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        stack = []
        ans = []
        curr = root
        while curr:
            while (curr.left):
                print
                curr.left.val, "l"
                stack.append(curr.left)
                curr = curr.left

            if curr.right:
                print
                curr.right.val, "r"
                stack.append(curr.right)
            print
            curr.val
            ans.append(curr.val)
            if stack:
                curr = stack.pop()
            else:
                curr = None
        return ans
        # return self.inorderTraversal( root.left)+[root.val]+self.inorderTraversal(root.right)

        """
        :type root: TreeNode
        :rtype: List[int]
        """

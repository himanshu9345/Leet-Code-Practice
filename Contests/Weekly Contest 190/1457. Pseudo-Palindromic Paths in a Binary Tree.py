# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorder(self, root, arr, val):             

        if root:
            arr[root.val - 1] += 1
            if root.left:
                self.inorder(root.left, arr, False)
            if root.right:
                self.inorder(root.right, arr, False)
            if not root.left and not root.right:
                count = 0
                for i in arr:
                    if i%2 == 1:
                        count +=1
                if (count == 1 or count == 0) :
                    self.ans += 1

            arr[root.val - 1] -= 1
        return                

    def pseudoPalindromicPaths (self, root):
        if not root:
            return 0
        self.ans = 0
        arr  = [0]*10
        self.inorder(root, arr, True)
        return self.ans
        # return self.ans/2
        """
        :type root: TreeNode
        :rtype: int
        """
        
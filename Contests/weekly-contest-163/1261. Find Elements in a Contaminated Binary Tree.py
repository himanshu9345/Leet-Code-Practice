# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def buildT(root):
    if not root:
        return None
    if root.left:
        root.left.val = 2 * root.val + 1
        buildT(root.left)
    if root.right:
        root.right.val = 2 * root.val + 2
        buildT(root.right)
    return root


def search(root, dict1):
    if not root:
        return False
    dict1.add(root.val)
    search(root.left, dict1)
    search(root.right, dict1)
    return dict1


class FindElements(object):

    def __init__(self, root):
        if root:
            root.val = 0
            self.root = buildT(root)
        else:
            self.root = None

        self.dict1 = search(self.root, set())
        """
        :type root: TreeNode
        """

    def find(self, target):
        return target in self.dict1

        """
        :type target: int
        :rtype: bool
        """

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
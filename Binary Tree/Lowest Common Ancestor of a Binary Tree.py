# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lca(root, p, q):  # O()
    if not root:
        return None
    node1 = lca(root.left, p, q)
    node2 = lca(root.right, p, q)
    if root == p or root == q:
        return root
    if not node1 and not node2:
        return None
    if node1 and node2:
        return root

    if node1:
        return node1
    else:
        return node2


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # seen=set([p,q])
        return lca(root, p, q)

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

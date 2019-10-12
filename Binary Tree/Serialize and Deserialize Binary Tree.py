# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def preorder(root):
    if not root:
        return ["*&"]
    return preorder(root.left) + preorder(root.right) + ["*" + str(root.val)]


def inorder(root):
    if not root:
        return ["*&"]
    return inorder(root.left) + ["*" + str(root.val)] + inorder(root.right)


def buildTree(il, pl):
    if il:
        el = pl.pop()
        if el == "&":
            return None
        index = il.index(el)
        root = TreeNode(int(il[index]))
        root.right = buildTree(il[index + 1:], pl)
        root.left = buildTree(il[:index], pl)
        return root


class Codec:

    def serialize(self, root):
        if not root:
            return "&"
        queue = [root]
        ans = [str(root.val)]
        while queue:
            new = []
            count = 0
            for i in queue:
                if i != "*":

                    if i.left:
                        ans.append(str(i.left.val))
                        new.append(i.left)
                    else:
                        ans.append("*")
                    if i.right:
                        ans.append(str(i.right.val))
                        new.append(i.right)
                    else:
                        ans.append("*")
                else:
                    count += 1
            if count == len(queue):
                queue = []
            else:
                queue = new

        return "&".join(ans)

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        if data == "&":
            return None
        # print data
        data = data.split("&")[::-1]
        root = TreeNode(int(data.pop()))
        queue = [root]
        while queue:
            new = []
            for i in queue:
                el = data.pop()
                if el != "*":
                    i.left = TreeNode(int(el))
                    new.append(i.left)
                el = data.pop()
                if el != "*":
                    i.right = TreeNode(int(el))
                    new.append(i.right)
            queue = new
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

#TLE
class Node(object):
    def __init__(self, n):
        self.left = None
        self.right = None
        self.val = n
        self.count = 1

import heapq

def insertBST(root, key):
    parent = None
    while root:
        if root.val > key:
            parent = root
            parent.count += 1
            root = root.left
            if not root:
                parent.left = Node(key)
        else:
            parent = root
            parent.count += 1
            root = root.right
            if not root:
                parent.right = Node(key)


def buildBST(k, nums):
    root = Node(nums[0])
    root1 = root
    for i in range(1, len(nums)):
        insertBST(root, nums[i])

    return root1


def getKthLargest(root, k):
    walker = root
    while k > 0:
        pos = 1
        if root.right:
            # print root.right.count
            pos += root.right.count
        if pos == k:
            break
        if pos < k:
            k -= pos
            root = root.left
        elif pos > k:
            root = root.right

    return root.val


class KthLargest(object):
    root = None
    k = None

    def __init__(self, k, nums):
        if len(nums) > 0:
            self.root = buildBST(k, nums)
        self.k = k

        """
        :type k: int
        :type nums: List[int]
        """

    def add(self, val):
        if not self.root:
            self.root = Node(val)
            return getKthLargest(self.root, self.k)
        insertBST(self.root, val)
        # print self.k,self.root.count
        return getKthLargest(self.root, self.k)
        """
        :type val: int
        :rtype: int
        """

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
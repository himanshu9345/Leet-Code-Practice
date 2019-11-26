class Node:
    def __init__(self):
        self.dict1 = {}
        self.sum = 0


class MapSum(object):

    def __init__(self):
        self.root = Node()
        self.seen = set()
        """
        Initialize your data structure here.
        """

    def insert(self, key, val):
        if key in self.seen:
            self.replace1(key, val)
            return
        node = self.root
        for c in key:
            if c in node.dict1:
                node = node.dict1[c]
                node.sum += val
            else:
                node.dict1[c] = Node()
                node = node.dict1[c]
                node.sum += val

        self.seen.add(key)

    def replace1(self, key, val):
        node = self.root
        for c in key:
            if c in node.dict1:
                node = node.dict1[c]
                node.sum = val
            else:
                node.sum = val
                node.dict1[c] = Node()
                node = node.dict1[c]

        """
        :type key: str
        :type val: int
        :rtype: None
        """

    def sum(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.dict1:
                return 0
            else:
                node = node.dict1[c]
        return node.sum
        """
        :type prefix: str
        :rtype: int
        """

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
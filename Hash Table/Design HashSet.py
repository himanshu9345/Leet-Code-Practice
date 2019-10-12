class MyHashSet(object):

    def __init__(self):
        self.list1 = [[]] * 1000
        """
        Initialize your data structure here.
        """

    def add(self, key):
        if not self.contains(key):
            self.list1[key % 1000].append(key)
        """
        :type key: int
        :rtype: None
        """

    def remove(self, key):
        if self.contains(key):
            self.list1[key % 1000].remove(key)

        """
        :type key: int
        :rtype: None
        """

    def contains(self, key):
        return key in self.list1[key % 1000]
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
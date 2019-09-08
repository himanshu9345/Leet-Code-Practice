import random


class RandomizedSet(object):

    def __init__(self):
        self.dict1 = {}
        self.list1 = []
        """
        Initialize your data structure here.
        """

    def insert(self, val):
        if val not in self.dict1:
            self.dict1[val] = len(self.list1)
            self.list1.append(val)
            return True
        else:
            return False
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

    def remove(self, val):
        if val in self.dict1:
            index = self.dict1[val]
            self.dict1[self.list1[-1]] = index
            self.list1[index] = self.list1[-1]
            self.list1.pop()
            # if self.list1!=[]:
            #     self.dict1[self.list1[index]]=index
            del self.dict1[val]
            return True
        else:
            return False
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

    def getRandom(self):
        rindex = random.randint(0, len(self.list1) - 1)
        return self.list1[rindex]
        """
        Get a random element from the set.
        :rtype: int
        """

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
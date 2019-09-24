class MinStack(object):

    def __init__(self):
        self.min1 = []
        self.stack = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.stack.append(x)
        if self.min1:
            if x <= self.min1[-1]:
                self.min1.append(x)
        else:
            self.min1.append(x)
        # print self.min1
        # print self.stack
        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        val = self.stack.pop()
        if self.stack:
            if val == self.min1[-1]:
                self.min1.pop()
        else:
            self.min1.pop()
        """
        :rtype: None
        """

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """

    def getMin(self):
        return self.min1[-1]
        """
        :rtype: int
        """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
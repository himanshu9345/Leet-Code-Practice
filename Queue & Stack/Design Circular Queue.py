class MyCircularQueue(object):

    def __init__(self, k):
        self.size = k
        self.list1 = [-1] * k
        self.front = -1
        self.rear = -1
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.list1[self.rear] = value
        return True
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.rear == self.front:
            self.front = -1
            self.rear = -1
            return True

        self.list1[self.front] = -1
        self.front = (self.front + 1) % self.size
        return True
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """

    def Front(self):
        return self.list1[self.front]
        """
        Get the front item from the queue.
        :rtype: int
        """

    def Rear(self):
        return self.list1[self.rear]

        """
        Get the last item from the queue.
        :rtype: int
        """

    def isEmpty(self):
        return self.front == -1
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """

    def isFull(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        else:
            return False
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
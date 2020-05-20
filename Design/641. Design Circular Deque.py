class Node(object):
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
class MyCircularDeque(object):

    def __init__(self, k):
        self.size = k
        self.currSize  = 0
        self.head = None
        self.end = None
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        

    def insertFront(self, value):
        if self.currSize >= self.size: return False
        
        self.currSize += 1
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next  = self.head
            self.head = new_node
            return True
        self.head = new_node
        self.end = new_node
        return True
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        

    def insertLast(self, value):
        if self.currSize >= self.size: return False
        
        self.currSize += 1
        new_node = Node(value)
        if self.end:
            self.end.next = new_node
            new_node.prev  = self.end
            self.end = new_node
            return True
        self.end = new_node
        self.head = new_node
        return True
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        

    def deleteFront(self):
        if not self.head:
            return False
        self.currSize -= 1
        if not self.head.next:
            self.end = None
            self.head = None
            return True
        self.head = self.head.next
        self.head.prev = None
        return True
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        

    def deleteLast(self):
        if not self.end:
            return False
        self.currSize -= 1
        if not self.end.prev:
            self.end = None
            self.head = None
            return True
        self.end = self.end.prev
        self.end.next = None
        return True
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        

    def getFront(self):
        if self.head :
            return self.head.val
        return -1
        """
        Get the front item from the deque.
        :rtype: int
        """
        

    def getRear(self):
        if self.end:
            return  self.end.val
        return -1
        """
        Get the last item from the deque.
        :rtype: int
        """
        

    def isEmpty(self):
        return self.currSize == 0
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        

    def isFull(self):
        return self.currSize == self.size
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
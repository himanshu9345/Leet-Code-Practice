class Node(object):
    val = None
    next = None
    prev = None

    def __init__(self, val):
        self.val = val


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        """
        Initialize your data structure here.
        """

    def get(self, index):

        if index > self.size or index < 0:
            return -1
        head1 = self.head
        while (index != 0):
            head1 = head1.next
            index -= 1
        # print(head1.val)
        if head1:
            return head1.val
        return -1


    def addAtHead(self, val):
        # print("ggH",self.size)

        new_head = Node(val)

        if not self.head:
            self.head = new_head
            self.size += 1

            return
        new_head.next = self.head
        self.head.prev = new_head

        self.head = new_head
        self.size += 1

        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """

    def addAtTail(self, val):
        self.size += 1
        head1 = self.head
        new_node = Node(val)
        if head1 == None:
            self.head = new_node
            return
        # if head1.next==None:
        #     head.next=new_node
        #     return
        # print("ggt",self.size)

        while (head1.next != None):
            head1 = head1.next
        # print (head1.val)
        head1.next = new_node
        new_node.prev = head1
        return

    def addAtIndex(self, index, val):
        # if index<0:
        #     return
        head1 = self.head
        # print("gg1",self.size)
        if index <= 0:
            self.addAtHead(val)
            return
        # if index==self.size:
        #     self.addAtTail(val)
        #     return

        if index > self.size:
            return
        count = 0

        while (head1 != None):
            if count == index:
                # print("h",head1.val)
                break
            head1 = head1.next
            count += 1
        # print(head1.prev.val,"hjkl")
        if not head1:
            self.addAtTail(val)
            return
        new_data = Node(val)
        new_data.next = head1
        new_data.prev = head1.prev
        head1.prev.next = new_data
        head1.prev = new_data

        # print(new_data.prev.next.val,self.head.next.val)
        self.size += 1

        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """

    def deleteAtIndex(self, index):
        if index < 0:
            return
        head1 = self.head
        # print("ggd",self.size)

        if index + 1 > self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return

        count = 0

        while (head1 != None):
            if count == index:
                break
            head1 = head1.next
            count += 1

        # while(index!=1):
        #     head1=head1.next
        #     index-=1
        head1.prev.next = head1.next
        if head1.next:
            head1.next.prev = head1.prev

        # head1.next=head1.next.next
        self.size -= 1

        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """

    def printlist(self):

        head1 = self.head
        while (head1 != None):
            print(head1.val, self.size)
            head1 = head1.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
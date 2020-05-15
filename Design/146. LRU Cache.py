class Node(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.value = val
        self.key = key

class LRUCache(object):
    
    def __init__(self, capacity):
        self.maxsize = capacity
        self.currentsize = 0
        # not null value of LinkedList
        self.end = None
        # head
        self.head = None
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key].value
        self.updateNode(value, self.cache[key])
        return value
        
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = self.updateNode(value, self.cache[key])
        else:
            self.cache[key] = self.addNode(key ,value)
    
    def updateNode(self, value, node):
        if node == self.end and node != self.head:
            self.end = node.prev
            self.end.next = node.next
        elif node != self.end and node != self.head:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        # pointing to head
        if node == self.head:
            node.value = value
        else:
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        
        node.value = value
        return node
    
    def deleteNode(self):
        if self.end and self.end.prev:
            del self.cache[self.end.key]
            self.end.prev.next = self.end.next
            if self.end.next:
                self.end.next.prev = self.end.prev
            self.currentsize -= 1
            self.end = self.end.prev
            return
        if self.end:
            del self.cache[self.end.key]
            self.currentsize -= 1
        self.end = None
        self.head = None
        return 
            
    # add a new node in LL
    def addNode(self, key, value):
        new_node = Node(key, value)
        
        if self.currentsize < self.maxsize:
            if self.head:
                self.head.prev = new_node
                new_node.next = self.head
            self.head = new_node
        else:
            self.deleteNode()
            if self.head:
                self.head.prev = new_node
                new_node.next = self.head
            self.head = new_node
        self.currentsize += 1
        if not self.end:
            self.end = new_node
        return new_node
        
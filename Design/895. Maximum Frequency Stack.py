# My Solution
class FreqStack(object):
        
    def __init__(self):
        self.dict1 = defaultdict(int)
        self.elno = 0
        self.heap = []

    def push(self, x):
        self.dict1[x] += 1
        self.elno += 1
        heapq.heappush(self.heap, (-self.dict1[x], -self.elno, x))
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        freq, no, val = heapq.heappop(self.heap)
        self.dict1[val] -= 1
        return val
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


class FreqStack(object):
        
    def __init__(self):
        self.dict1 = defaultdict(int)
        self.val = defaultdict(list)
        self.maxfreq = float('-inf')

    def push(self, x):
        
        self.dict1[x] += 1
        if self.dict1[x]>self.maxfreq:
            self.maxfreq = self.dict1[x]
        self.val[self.dict1[x]].append(x)
        # heapq.heappush(self.heap, (-self.dict1[x], -self.elno, x))
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        res = self.val[self.maxfreq].pop()
        self.dict1[res] -= 1
        if not self.val[self.maxfreq]:
            self.maxfreq -= 1
        return res
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
#My Solution TLE
class TreeAncestor(object):

    def __init__(self, n, parent):
        # height of tree
        max_depth = 17
        arr = [[-1] * max_depth for _ in range(n)]
        arr[0][0] = 0
        for i in range(1, n):
            arr[i][0] = i
            for j in range(1, max_depth):
                arr[i][j] = arr[parent[i]][j-1]
        self.arr = arr
        
        # self.parent = parent
        # self.n = n
        # self.dict1 = defaultdict(list)
        # self.pc = defaultdict(list)
        # for i,v in enumerate(parent):
        #     self.pc[v].append(i)
        # self.dict1[0] = [0]
        # queue = [0]
        # while queue:
        #     nxt_lvl = []
        #     for i in queue:
        #         for child in self.pc[i]:
        #             self.dict1[child] = [child]+self.dict1[parent[child]]
        #             nxt_lvl.append(child)
        #     queue = nxt_lvl
        # # print self.dict1
                    
        """
        :type n: int
        :type parent: List[int]
        """
        

    def getKthAncestor(self, node, k):
        
        while k>=17 and node!=-1:
            node = self.arr[node][16]
            k -= 16
        if node != -1:
            return self.arr[node][k]
        else:
            return  -1
        
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
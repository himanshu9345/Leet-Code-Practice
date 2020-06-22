class Solution(object):
    def findMST(self, edges, include, exclude, n):
        seen = [-1]*n
        count = n
        # UF to track for connected graph
        def parent(arr, i):
            if arr[i] == -1:
                return i
            return parent(arr, arr[i])
        
        def union(arr, i, j):
            pi = parent(arr,i)
            pj = parent(arr,j)
            if pi!=pj:
                arr[pj] = pi
                return pi
            return  pi
        
        # include initial edges
        cost = 0
        for i,j,c in include:
            union(seen,i,j)
            count -= 1
            cost += c
        # heap to run prim's greedy algo
        heap = []
        for a,b,c in edges:
            if (a,b) != exclude:
                heapq.heappush(heap, (c,a,b))
        
        while heap:
            c, a, b =heapq.heappop(heap)
            # if parent are same then vercites a and b are connected
            if parent(seen, a) != parent(seen,b):
                union(seen, a,b)
                count -=1
                cost += c
        # if there are more than one connected component 
        # the graph is biparted so infinite cost tomake it connected graph
        # or MST
        if count >1:
            return  float('inf')
        
        return cost
            
        
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # MST on whole graph
        ic = self.findMST(edges,[],-1,n)
        # list to store critical and pseudo-critical edges
        ce = []
        pce = []
        # to track edges index
        idx = 0
        for i, j, c in edges:
            # cost with including that edge
            cost = self.findMST(edges, [], (i,j), n)
            if cost == 0 or cost > ic:
                # if cost is greater the that is CE
                ce.append(idx)
            else:
                # cost with excluding that edge
                cost = self.findMST(edges, [[i,j,c]], -1, n)
                if cost == ic:
                    # removing edge i,j also give MST so i,j pseudo critical
                    pce.append(idx)
            idx += 1
        return [ce,pce]
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # array to store prices to travel i'th city from source
        ans = [float('inf') for _ in range(n)]
        # source is 0 distance from itself
        ans[src] = 0
        # saving prices of next cities from source
        for i, j, k in flights:
            if i == src:
                ans[j] = k
        '''
        In bellman to find shortest path from A to B
        to find global shorted path we loop n-1(n is vertices) time and iterate 
        over all the edges(flights) but in this questions we are asked to find shortest path
        only if we loop though on K times
        '''
        for k in range(K):
            # Saving previous state copy
            curr = ans[::]
            for i, j, price in flights:
                # check if current project from i to j is less then 
                # previous iteration node ith price and price btw i-j
                curr[j] = min(curr[j], ans[i] + price)
            ans = curr[::]
        
        return ans[dst] if ans[dst] != float('inf') else -1
        
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        
        graph = defaultdict(list)
        for i, j, price in flights:
            graph[i].append((j,price))
        
        '''
        applying dijkstra shortest path till we make K 
        hops from source city, if we find dst city till K hops
        return that price. 
        '''
        heap = [(0, src, -1)]
        
        while heap:
            p, city, k = heapq.heappop(heap)
            if city == dst:
                return p
            if k < K:    
                for d, price in graph[city]:
                        heapq.heappush(heap, (p + price, d, k + 1))
            
        return -1
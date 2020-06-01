class Solution(object):
    def minReorder(self, n, connections):
        graph = defaultdict(list)
        rev = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            rev[j].append(i)
        self.count = 0
        visited = [0 for i in range(n)]
        
        def bfs(node):
            queue = [node]
            while queue:
                next1 = []
                for i in queue:
                    for j in rev[i]:
                        if i!=j and not visited[j] :
                            next1.append(j)
                            visited[j] = 1
                    for j in graph[i]:
                        if j !=i and not visited[j]:
                            self.count += 1
                            next1.append(j)
                            visited[j] = 1
                queue = next1
        
        visited[0] = 1
        bfs(0)
        return self.count
           
                
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
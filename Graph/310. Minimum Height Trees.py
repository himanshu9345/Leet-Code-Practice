class Solution(object):
        
    def findMinHeightTrees(self, n, edges):
        
        graph = defaultdict(list)
        degree = [0 for i in range(n)]
        visited = [0 for i in range(n)]
        totale = 0
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            degree[i] += 1
            degree[j] += 1
            totale += 1

        leaves = []
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        while totale >= 2:
            new_leaves =[]
            for i in leaves:
                visited[i] = 1
                degree[i] = 0
                totale -= 1
                for root in graph[i]:
                    if degree[root] > 1:
                        degree[root] -= 1
                    if degree[root] == 1:
                        new_leaves.append(root)
            leaves =  new_leaves
        return [i for i in range(n) if visited[i] == 0]

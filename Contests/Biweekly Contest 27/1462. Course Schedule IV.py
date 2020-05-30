class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        graph = defaultdict(list)
        for i,j in prerequisites:
            graph[j].append(i)
        
        visited = [0 for i in range(n)]
        preqarr = defaultdict(set)
        
        def combine(i):
            if visited[i]:
                return
            for j in graph[i]:
                preqarr[i].add(j)
                combine(j)
                preqarr[i] = preqarr[i].union(preqarr[j])
            visited[i] = 1 
            return 
          
            
        for i in  range(n):
            if not  visited[i]:
                combine(i)
  
        res = []    
        for i,j in queries:
            if i in preqarr[j]:    
                res.append(True)
            else:
                res.append(False)

        return res
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
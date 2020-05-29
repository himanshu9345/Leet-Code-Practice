class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dict1 = defaultdict(list)
        for i, j in prerequisites:
            dict1[i].append(j)
        
        result = [i for i in range(numCourses) if i not in dict1]
        visited = [0 if i in dict1 else 1 for i in range(numCourses) ]
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                # result.append(node)
                return True
            visited[node] = -1
            
            for i in dict1[node]:
                if not dfs(i):
                    return []
            if visited[node] != 1:
                result.append(node)
            visited[node] = 1
            return True
        
        for i  in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
                # print result
        print result
        return result
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dict1 = defaultdict(list)
        for i, j in prerequisites:
            dict1[i].append(j)
        result = []
        visited = [0 for i in range(numCourses)]
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                result.append(node)
                return True
            visited[node] = -1
            
            for i in dict1[node]:
                if not dfs(i):
                    return False
            result.append(node)
            visited[node] = 1
            return True
        for i  in range(numCourses):
            if not dfs(i):
                return False
        print result
        return True
#         white = set()
#         black = set()
#         gray = set()
        
#         def dfs(node):
#             gray.add(node)
#             for i in dict1[node]:
#                 if i in gray:
#                     return False
#                 if i in black:
#                     continue
#                 if not dfs(i):
#                     return False
#             gray.remove(node)
#             black.add(node)
#             return True
        
#         for i in range(numCourses):
#             if i not in black:
#                 if not dfs(i):
#                     return False
#         return True
# #         visited = set()
# #         stack = []
# #         def dfs(course):
# #             visited.add(course)
# #             for c in dict1[course]:
                
# #                 if c in grey:
# #                     return False
                
                
# #                 if c not in visited:
# #                     dfs(c)
# #             stack.append(course)
# #             return
        
                
        
# #         for i in range(numCourses):
# #             if i not in visited:
# #                 dfs(i)
# #             print stack
# #         return len(stack) == numCourses        
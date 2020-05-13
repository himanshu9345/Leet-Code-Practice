class Solution(object):
    walk=0
    def minTime(self, n, edges, hasApple):
        dict1 = {}
        for i, j in edges:
            if i in dict1:
                dict1[i].append(j)
            else:
                dict1[i]=[j]
        
        def dfs(dict1,root,dist):
            #return if any apple were found in this edge
            if root in dict1:
                
                dist=0
                for i in dict1[root]:
                    if hasApple[i]:
                        # print(i,"add")
                        dist+=2
                    subtreewalk = dfs(dict1,i,0)
                    if subtreewalk>0 and not hasApple[i]:
                        # print(i,"add1",subtreewalk)
                        subtreewalk+=2
                    dist+=subtreewalk
                    # print(dist,i)
                if dist==0:
                    return 0
                return dist
            return 0
                        
        return dfs(dict1,0,0)

        
# class Solution(object):
#     walk=0
#     def minTime(self, n, edges, hasApple):
#         dict1={}
#         for i,j in edges:
#             if i in dict1:
#                 dict1[i].append(j)
#             else:
#                 dict1[i]=[j]
        
#         def dfs(dict1,root,dist,apple):
#             print (root,dist,self.walk)
#             if root not in dict1:
#                 return apple
#             flag=True
#             apple=False
#             for i in dict1[root]:
#                 print i,hasApple[i],root,flag,self.walk
#                 if hasApple[i]:
#                     if flag:
#                         self.walk+=dist
#                         flag=False
#                     else:
#                         self.walk+=2
#                     dist=0
#                     apple=True
                
#                 val = dfs(dict1,i,dist+2,apple)
#                 if val or apple:
#                     apple=True
#                 if apple:
#                     flag=False
#             return apple
#         dfs(dict1,0,2,False)
#         return self.walk
                    

    



       
       
        
       
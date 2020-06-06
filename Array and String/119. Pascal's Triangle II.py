class Solution(object):
    def getRow(self, rowIndex):
#         ans=[]
        
#         if rowIndex==0:
#             return [1]
#         # if rowIndex==1:
#         #     return [[1]][-1]
#         ans=[[1],[1,1]]
#         if rowIndex==1:
#             return ans[-1]
#         for i in range(2,rowIndex+1):
#             ans1=[1]
#             for j in range(i-1):
#                 ans1.append(ans[i-1][j]+ans[i-1][j+1])
#             ans1.append(1)
#             ans.append(ans1)
#         return ans[-1]
        def helper(i):
            if i == 0:
                return [1]
            
            ans = [1]
            prev = helper(i-1)
            prev_el = prev[0]
            for i in prev[1:]:
                ans.append(prev_el + i)
                prev_el = i
            ans += [1]
            return ans
        if rowIndex == 0:
            return [1]
        ans = [1,1]
        prev_lvl = []
        for i in range(2, rowIndex+1):
            prev_lvl = [1]
            prev = ans[0]
            for i in ans[1:]:
                prev_lvl.append(prev + i)
                prev = i
            prev_lvl.append(1)
            ans = prev_lvl
        return ans
        # return helper(rowIndex)
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
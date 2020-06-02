class Solution(object):
    def tracepath(self, grid,dp,m,n):
        sx, sy = m, n 
        start = dp[sx][sy]
        while start != 0 and start != -100000:
            grid[sx-1][sy-1] = 0
            newlx ,newly = sx, sy-1
            newux, newuy = sx - 1, sy
            # print sx, sy, start, dp[sx][sy], dp[newlx][newly],dp[newux][newuy]

            if dp[newlx][newly]+1 == dp[sx][sy]:
                    sx, sy = newlx, newly   
            elif dp[newux][newuy]+1 == dp[sx][sy]:
                    sx, sy = newux, newuy
            # print sx, sy, start, dp[sx][sy]
            start -= 1
    def memofun(self, dp, grid, r1, c1, c2, n):
        r2 = r1 + c1 - c2
        
        if r1 >= n or c1 >= n or c2 >= n or r2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')
        
        if dp[r1][c1][c2] != -1:
            return dp[r1][c1][c2]
        
        if c1 == n-1 and r1 == n-1:
            return grid[r1][c1]
        
        ans = 0 
        if c1 != c2:
            ans += grid[r2][c2]
        dp[r1][c1][c2] = grid[r1][c1] + max(self.memofun(dp, grid, r1 + 1 , c1, c2, n) , self.memofun(dp, grid, r1 + 1, c1, c2 + 1, n) , self.memofun(dp, grid, r1, c1 + 1, c2 + 1, n) , self.memofun(dp, grid, r1, c1 + 1, c2, n))  + ans
        
        return dp[r1][c1][c2]
        
        
        
    def cherryPickup(self, grid):
        m = len(grid)
        n = len(grid[0])
        
#         dp = [[[-1]*(n+1) for i in range(m+1)] for i in range(m+1)]
        
#         seen = set()
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if grid[i-1][j-1] != -1:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        
#         self.tracepath(grid, dp, m,n)
#         sum1 = dp[m][n]
#         print grid
#         print dp
        dp = [[[-1]*(n) for i in range(m)] for i in range(m)]
        return max(0, self.memofun(dp, grid, 0, 0, 0, m))
        
        # for i in range(m, 0, -1):
        #     for j in range(n, 0 , -1):
        #         if grid[i-1][j-1] != -1:
        #             max1 = dp[i][j]
        #             if i+1<=m:
        #                 max1 = max(max1, dp[i+1][j])
        #             if j+1<=n:
        #                 max1 = max(max1, dp[i][j+1])
        #             dp[i][j] = max1 + grid[i-1][j-1]
        # print dp
        # sum1 += dp[1][1]
        # if sum1 > 0:
        #     return sum1 
        # return 0
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
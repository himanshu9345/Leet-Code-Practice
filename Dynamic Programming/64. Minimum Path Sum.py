class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n + 1) for i in range(m + 1)]
        dp[0][1], dp[1][0] = 0, 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
                
        return dp[m][n]
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
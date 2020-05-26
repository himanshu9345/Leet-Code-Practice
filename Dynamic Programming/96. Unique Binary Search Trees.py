class Solution(object):
    def numTrees(self, n):
        if n < 2:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        
        return dp[n]
        
        
        """
        :type n: int
        :rtype: int
        """
        
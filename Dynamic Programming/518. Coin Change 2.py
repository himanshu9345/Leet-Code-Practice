class Solution(object):
    def change(self, amount, coins):
        
        dp = []
        for i in range(0, len(coins)+1):
            new = []
            for j in range(0, amount+1):
                if j == 0:
                    new.append(1)
                else:
                    new.append(0)
            dp.append(new)
        
        for j in range(1, amount + 1):
            for i in range(1, len(coins) + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print dp
        return dp[len(coins)][amount]
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
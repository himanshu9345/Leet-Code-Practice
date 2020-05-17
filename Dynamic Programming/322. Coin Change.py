class Solution(object): # more optimal was dfs
    def coinChange(self, coins, amount):
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for x in xrange(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
class Solution(object): #least optimal than above
    def coinChange(self, coins, amount):
        dp = []
        for i in range(0, amount + 1):
            new = []
            for j in range(0,len(coins)+1):
                
                new.append(0)
                if j == 0:
                    new[0] = 1000000000

            dp.append(new)
        # print dp
        for i in range(1, amount + 1):
            for j in range(1, len(coins)+1):
                if i>=coins[j-1]:
                    dp[i][j] = min(dp[i - coins[j - 1]][j ] + 1, dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]
                    
                
        # print dp
        if dp[amount][len(coins)] == 1000000000:
            return -1
        return dp[amount][len(coins)]
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
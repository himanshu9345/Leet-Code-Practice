class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = []
        for i in range(m+1):
            new1 = []
            for j in range(n+1):
                if j == 0:
                    new1.append(i)
                elif i == 0:
                    new1.append(j)
                else:
                    new1.append(0)
            dp.append(new1)
        # print dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                # print word1[j-1], word2[i-1],j,i
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[m][n]
                    

            
        
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
def minCostII( costs):
        # write your code here
        if not costs:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        m = len(costs)
        n = len(costs[0])
        
        m1, m2 = float('inf'), float('inf')
        m1i = -1
        m2i = -1
            
        dp = [[float('inf')]*n for _ in range(m+1)]
        for i in range(n):
            dp[1][i] =costs[0][i]
        print (dp)

        minarr = [float('inf')]*n
        for i in range(2, m+1):
            m1, m2 = float('inf'), float('inf')
            m1i = -1
            m2i = -1
            for k, v in enumerate(dp[i-1]):
                x=v
                if x <= m1:
                    m1, m2 = x, m1
                    m1i, m2i = k, m1i
                elif x < m2:
                    m2 = x
                    m2i = k
            for j in range(n):
                if m1i == j:
                    dp[i][j] = costs[i-1][j] + m2
                else:
                    dp[i][j] = costs[i-1][j] + m1
            
            print (dp)
        return min(dp[m])

costs = [[14,2,2],[4,4,5],[14,3,10]]
print(minCostII( costs))
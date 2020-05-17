class Solution(object):
    def climbStairs(self, n):
        stairs = [0] * (n+1)
        
        if n <= 1:
            return 1
        if n == 2:
            return 2
        stairs[1] = 1
        stairs[2] = 2
        
        for i in range(3, n+1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        # print stairs
        return stairs[n]
        """
        :type n: int
        :rtype: int
        """
        
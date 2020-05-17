class Solution(object):
    def fib(self, N):
        if N == 0:
            return 0
        ans = [0] * (N + 1)
        ans[1] = 1
        for i in xrange(2, N + 1):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[N]
        """
        :type N: int
        :rtype: int
        """
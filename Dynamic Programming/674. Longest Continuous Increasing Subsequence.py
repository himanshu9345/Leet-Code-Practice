class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        prev = -1
        for i in range(n):
            if prev!= -1 and nums[prev] < nums[i] :
                dp[i] = dp[prev] + 1
            prev = i
        return max(dp)
        """
        :type nums: List[int]
        :rtype: int
        """
        
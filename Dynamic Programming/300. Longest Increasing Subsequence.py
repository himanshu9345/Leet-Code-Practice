class Solution(object):
    def helper(self, nums, i, prev):
        if i >= len(nums):
            return 0
        
        ans = 0
        if prev<nums[i] or prev == -1:
            ans = 1 + self.helper(nums, i + 1, nums[i])
        # print ans, nums[i], prev,  i
        return max(self.helper(nums, i + 1, prev), ans)
        
                    
    def lengthOfLIS(self, nums): # TLE
        dict1 = {}
        return self.helper(nums, 0, -1)

    
    def helper(self, nums, i, prev, dp):
        if i >= len(nums):
            return 0
        if dp[i][prev+1] >= 0:
            return dp[i][prev+1]
        ans = 0
        if nums[prev]<nums[i] or prev <= -1:
            ans = 1 + self.helper(nums, i + 1, i, dp)
        # print ans, nums[i], prev,  i
        dp[i][prev + 1] =max(self.helper(nums, i + 1, prev, dp), ans)
        return dp[i][prev + 1]
        
                    
    def lengthOfLIS(self, nums): # TLE
        if not nums:
            return 0
        n = len(nums)
        dp = [[-1]*(n+1) for i in range(n)]
        return self.helper(nums, 0, -1, dp)
    
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [0]*(n)
        dp_len = 0
        for i in nums:
            left = bisect.bisect_left(dp, i, 0, dp_len)
            dp[left] = i
            if left == dp_len:
                dp_len += 1
        return dp_len
    
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*(n)
        # return self.helper(nums, 0, -1, dp)
        max2 = 0
        for i in range(len(nums)):
            max1 = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
            
        return max(dp)
    
class Solution(object):
    def helper(self, nums, i, prev):
        if i >= len(nums):
            return 0
        
        ans = 0
        if prev<nums[i] or prev == -1:
            ans = 1 + self.helper(nums, i + 1, nums[i])
        # print ans, nums[i], prev,  i
        return max(self.helper(nums, i + 1, prev), ans)
        
                    
    def lengthOfLIS(self, nums):
        dict1 = {}
        return self.helper(nums, 0, -1)
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
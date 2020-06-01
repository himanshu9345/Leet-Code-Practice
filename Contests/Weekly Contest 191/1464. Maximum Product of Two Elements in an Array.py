class Solution(object):
    def maxProduct(self, nums):
        max1 = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    max1 = max(max1, (nums[i]-1)*(nums[j]-1))
        return max1
        """
        :type nums: List[int]
        :rtype: int
        """
        
class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}
        count = 0
        for i in nums:
            if target - i in dict1:
                return [dict1[target - i], count]
            dict1[i] = count
            count += 1

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

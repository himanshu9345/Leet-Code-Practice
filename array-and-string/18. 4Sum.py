class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        ans = []
        dict1 = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    # print i,j,start,end
                    sum1 = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum1 == target:
                        dict1[(nums[i], nums[j], nums[start], nums[end])] = 1
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif sum1 > target:
                        end -= 1
                    else:
                        start += 1
        return dict1.keys()

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

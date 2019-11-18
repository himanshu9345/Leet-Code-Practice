class Solution(object):
    def threeSum(self, nums):

        if len(nums) < 3:
            return []
        i = 0
        j = 0
        ans = []
        seen = set(nums)
        nums = sorted(nums)
        while i < len(nums) - 1:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum1 = -nums[j] - nums[k]
                if sum1 == nums[i]:
                    ans.append([nums[j], nums[k], nums[i]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
                elif sum1 > nums[i]:
                    j += 1
                else:
                    k -= 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            i += 1
        return ans
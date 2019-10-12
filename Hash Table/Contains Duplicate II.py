class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict1 = {
        }
        for i, key in enumerate(nums):
            if key in dict1:
                # print k,i,dict1[key]
                if i - dict1[key] <= k:
                    return True
                else:
                    dict1[key] = i
            else:
                dict1[key] = i
        return False

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

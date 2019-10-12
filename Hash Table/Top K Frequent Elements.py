from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        dict1 = Counter(nums)
        ans = []
        # sorted(dict1.items(), key=lambda t: t[0])
        return [i for i, j in dict1.most_common(k)]

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

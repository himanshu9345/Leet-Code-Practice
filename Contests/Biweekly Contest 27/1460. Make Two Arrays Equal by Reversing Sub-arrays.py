class Solution(object):
    def canBeEqual(self, target, arr):
        return set(target) == set(arr)
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
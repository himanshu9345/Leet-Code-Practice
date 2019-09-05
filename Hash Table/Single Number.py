class Solution(object):
    def singleNumber(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
        if seen:
            return list(seen)[0]
        else:
            return 0
        """
        :type nums: List[int]
        :rtype: int
        """

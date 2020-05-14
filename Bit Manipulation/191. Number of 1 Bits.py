class Solution(object):
    def hammingWeight(self, n):
        num = n
        count=0
        while num:
            num = num & (num - 1)
            count += 1
        return count
        """
        :type n: int
        :rtype: int
        """
        
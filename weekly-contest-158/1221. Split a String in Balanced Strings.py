class Solution(object):
    def balancedStringSplit(self, s):
        r = 0
        # l=0
        count = 0
        for i in s:
            if i == "R":
                r += 1
            if i == "L":
                r -= 1
            if r == 0:
                count += 1
        return count
        """
        :type s: str
        :rtype: int
        """

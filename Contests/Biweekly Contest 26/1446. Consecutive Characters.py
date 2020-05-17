class Solution(object):
    def maxPower(self, s):
        max1 = 1
        count = 1
        prev = s[0]
        for i in s[1:]:
            if prev == i:
                count += 1
            else:
                count = 1
            max1 = max(max1, count)
            prev = i
        return max1
            
        """
        :type s: str
        :rtype: int
        """
        
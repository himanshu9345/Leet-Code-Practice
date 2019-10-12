class Solution(object):
    def firstUniqChar(self, s):
        dict1 = {}
        for i, k in enumerate(list(s)):
            if k in dict1:
                dict1[k] = -1
            else:
                dict1[k] = i
        min1 = 100000000
        for i in dict1:
            if dict1[i] >= 0:
                min1 = min(min1, dict1[i])
        if min1 == 100000000:
            return -1
        return min1
        """
        :type s: str
        :rtype: int
        """

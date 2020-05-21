from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        c = Counter(s)
        t = Counter(t)
        temp = 0
        for key in c:
            if key in t:
                temp += max(c[key] - t[key], 0)
            else:
                temp += c[key]
        return temp
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
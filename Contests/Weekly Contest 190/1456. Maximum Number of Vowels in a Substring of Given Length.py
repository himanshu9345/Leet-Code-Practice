class Solution(object):
    def maxVowels(self, s, k):
        j = 0
        curr_count = 0
        max1  = 0
        for i in range(len(s)):
            if i>=k:
                if s[j] in ['a','e', 'i', 'o', 'u']:
                    curr_count -= 1
                j += 1
            if s[i] in ['a','e', 'i', 'o', 'u']:
                curr_count += 1
            max1 = max(max1, curr_count)
        return max1
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
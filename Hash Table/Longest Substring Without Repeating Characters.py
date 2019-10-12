class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        dict1 = {}
        max1 = 0
        seen = set()
        while (i < len(s)):
            # print s[i]
            if s[i] in seen:
                i = dict1[s[i]]
                # print i,"i"
                del dict1[s[i]]
                max1 = max(max1, len(seen))
                seen.clear()
            else:
                seen.add(s[i])
                dict1[s[i]] = i
            i += 1
            # print(seen)
        return max(max1, len(seen))
        """
        :type s: str
        :rtype: int
        """

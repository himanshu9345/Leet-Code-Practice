class Solution(object):
    def hasAllCodes(self, s, k):
        all_str = set()
        str1 = ""
        for i in range(len(s)):
            str1 += s[i]
            if i >= k-1:
                all_str.add(str1)
                str1 = str1[1:]

        return len(all_str) == 2**k
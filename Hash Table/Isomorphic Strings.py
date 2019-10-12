class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        mapped = {}
        seen = set()
        for index, key in enumerate(list(s)):
            # print key,mapped
            if key in mapped:
                # print mapped[key],t[index]
                if t[index] != mapped[key]:
                    return False
            else:
                if t[index] not in seen:
                    mapped[key] = t[index]
                    seen.add(t[index])
                else:
                    return False

        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

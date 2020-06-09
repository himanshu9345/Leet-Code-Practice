class Solution(object):
    def isSubsequence(self, s, t):
        if s == t or (s == ""):
            return True
        if t == "":
            return False
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

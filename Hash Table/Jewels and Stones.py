class Solution(object):
    def numJewelsInStones(self, J, S):
        j = set(list(J))
        total = 0
        for i in S:
            if i in j:
                total += 1
        return total
        """
        :type J: str
        :type S: str
        :rtype: int
        """

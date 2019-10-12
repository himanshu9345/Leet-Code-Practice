class Solution(object):
    def isHappy(self, n):
        seen = set()
        while (True):
            list1 = list(str(n))
            newn = 0
            for i in list1:
                newn += int(i) * int(i)
            # print(newn)
            if newn == 1:
                return True
            if newn in seen:
                return False
            else:
                seen.add(newn)
            n = newn
        """
        :type n: int
        :rtype: bool
        """

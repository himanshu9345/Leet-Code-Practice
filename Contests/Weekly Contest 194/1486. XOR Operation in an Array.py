class Solution(object):
    def xorOperation(self, n, start):
        nums = []
        xor = start  
        for i in range(1, n):
            # print 2*i +start
            xor^=2*i + start
        return xor
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
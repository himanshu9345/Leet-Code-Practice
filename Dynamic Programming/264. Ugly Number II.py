# My aproach TLE
class Solution(object):
    def newIdea(self, n):
        if n in self.ugly:
            return self.ugly[n]
        if n==0:
            return False
        if n<3:
            return True
        isFalse = False
        for i in [2,3,5]:
            if n%i == 0:
                # print n,i
                isFalse = isFalse or self.newIdea(n/i)
        return isFalse
    
    def nthUglyNumber(self, n):
        self.ugly = {}
        
        i=1
        
        while len(self.ugly) != n:
            result = self.newIdea(i)
            # print i, result
            if result:
                self.ugly[i] = result
            i += 1
        return i-1
        """
        :type n: int
        :rtype: int
        """

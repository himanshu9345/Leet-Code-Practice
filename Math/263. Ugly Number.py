# 62% 
class Solution(object):
    def newIdea(self, n):
        if n==0:
            return False
        if n<3:
            return True
        isFalse = False
        for i in [2,3,5]:
            if n%i == 0:
                isFalse = isFalse or self.newIdea(n/i)
        return isFalse
    def isUgly(self, num):
        if num<0:
            return False
        return self.newIdea(num)

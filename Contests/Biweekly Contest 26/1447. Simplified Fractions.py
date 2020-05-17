class Solution(object):
    def simplifiedFractions(self, n):
        seen = set()
        ans = [] 
        for i in xrange(1, n):
            for j in xrange(1, n+1):
                j1 = j + 0.0
                if (i/j1)!=0 and (i/j1)<1:
                    # print (i/j1)
                    div = i/j1
                    if div not in seen:
                        seen.add(div)
                        ans.append(str(i)+"/"+str(j))
        return ans
        """
        :type n: int
        :rtype: List[str]
        """
        
class Solution(object):
    def kthGrammar(self, N, K):
        
        def helper(N, K):
            if N == 0:
                return  "0"
            
            ans  = helper(N-1, (K+1)/2)
            if ans  == "0":
                return "01"[(K-1)%2]
            else:
                return "10"[(K-1)%2]
        return helper(N, K)
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        
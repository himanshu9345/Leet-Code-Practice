class Solution(object):
    def printDivisors(self, n, list1) : 
      
        # Note that this loop runs till square root 
        i = 1
        while i <= math.sqrt(n): 

            if (n % i == 0) : 

                # If divisors are equal, print only one 
                if (n / i == i) : 
                    list1.append(i) 
                else : 
                    # Otherwise print both 
                    list1.append(i)
                    list1.append(n/i)

            i = i + 1

    def kthFactor(self, n, k):
        list1 = []
        self.printDivisors(n, list1)
        list1.sort()
        try:
            return list1[k-1]
        except:
            return -1
        
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
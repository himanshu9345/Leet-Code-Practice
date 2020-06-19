class Solution(object):
    def hIndex(self, citations):
        '''
        binary search O(logn)
        '''
        # left pointer
        l = 0
        # right pointer
        r = len(citations)-1
        # count for H-Index
        count = 0
        while l <= r:
            #getting the index middle citations 
            mid = l + (r-l)/2
            '''
            two case
            1. if we reach middle and citation value it greater than count(distance 
            from middle to end) then we are fine and try to find other citations 
            in left part
            2. if not then we will substract the current count(distance 
            from middle to end(r)) and trverse to right side of  the array.
            '''
            count += r - (mid + 1)
            
            if citations[mid] >= count:
                r = mid-1
            else:
                count -= r - (mid + 1)
                l = mid + 1
        return count            
        """
        :type citations: List[int]
        :rtype: int
        """
class Solution(object):
    def hIndex(self, citations):
        '''
        linear search from back O(n)
        '''
        count = 0
        while citations:
            if citations[-1]>count:
                count+=1
            else:
                return count
            citations.pop()
        return 0
        """
        :type citations: List[int]
        :rtype: int
        """
        
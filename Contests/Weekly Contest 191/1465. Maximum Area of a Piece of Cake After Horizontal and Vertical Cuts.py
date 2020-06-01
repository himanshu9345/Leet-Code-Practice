class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        prev = horizontalCuts[0]
        maxh = prev

        for i in horizontalCuts[1:]:
            maxh = max(maxh, i - prev)
            prev  = i
        
        maxh = max(maxh, h - prev)
        
        prev = verticalCuts[0]
        maxv = prev

        for i in verticalCuts[1:]:
            maxv = max(maxv, i - prev)
            prev  = i
        maxv = max(maxv, w - prev)
        # print prev

        return (maxv*maxh)%1000000007
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
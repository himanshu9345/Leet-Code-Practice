class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return  0
        n = len(envelopes)
        envelopes = sorted(envelopes,key = lambda x:(x[0], - x[1])) # sort 1st index as it is , but 2nd index as largest to smallest
        dp = [0] * (n )
        dp_len = 0
        for i  in range( n):
            # bisect_right gives next index to matching right most element
            left = bisect.bisect_left(dp, envelopes[i][1], 0, dp_len ) # does binary search gives the left most index where value couldb be inserted
            dp[left] = envelopes[i][1]
            if left == dp_len:
                dp_len += 1
            # print dp, dp_len, left, envelopes[i]
        return dp_len

        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
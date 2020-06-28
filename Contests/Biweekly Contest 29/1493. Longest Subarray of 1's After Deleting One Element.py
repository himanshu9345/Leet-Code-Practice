class Solution(object):
    def longestSubarray(self, nums):
        arr = nums[::]
        for i in range(1,len(nums)):
            if arr[i] == 0:
                continue
            arr[i] = arr[i] + arr[i-1]
        # print arr
        bk = nums[::]
        for i in range(len(nums)-2,-1,-1):
            if bk[i] == 0:
                continue
            bk[i] = bk[i] + bk[i+1]
        # print bk
        sum1 = 0
        for i in range(1,len(nums)-1):
            sum1 = max(sum1, bk[i+1]+arr[i-1])
        return sum1
        """
        :type nums: List[int]
        :rtype: int
        """
        
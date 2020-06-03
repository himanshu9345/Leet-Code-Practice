class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*(n)
        
#         dp_len = 0
#         for i in nums:
#             left = bisect.bisect_left(dp, i, 0, dp_len)
            
#             dp[left] = i
#             if left == dp_len:
#                 dp_len += 1
#             else:
#                 print dp,left,dp_len
            
#         # return self.helper(nums, 0, -1, dp)
        count = [1] * n # if we find same lenght lis  gain then add count[j] to count[i]
        max2 = 0
        for i in range(len(nums)):
            max1 = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp = [1,2,3,3,4(curr)]
                    #count = [1,1,1,1,1]
                    if dp[i] <= dp[j]:# if the number 1 > numb2 then dp array should get updated, and count of numb2 will be copied to numb1
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    # dp = [1,2,3,3,4(curr)]
                    #count = [1,1,1,1,2]
                    elif dp[i] == dp[j] + 1: # we cound lis 1 smaller then numb1 current len then that lis count should be added.
                        count[i] += count[j]
            # print dp,count
        max1 = max(dp)
        # print count, max1
        return sum([v for i,v in enumerate(count) if dp[i] == max1])
#         print dp
        
#         prev = []
#         i = 1
#         while i < n:
#             if prev = [] :
                
                
        # return dp_len
        
#         n = len(nums)
#         dp = [1]*n
#         for i in range(n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     prev = dp[i]
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     if dp[i] == prev:
#                         print "we can do", i,j,nums[i],nums[j]
#                     else:
#                         print "gg"
#         print dp
#         # return dp.count(max(dp))
#         max1 = max(dp)
#         dict1 = defaultdict(int)
#         count = 0
#         for i in dp:
#             if i == max1:
#                 prd = 1
#                 for keys in dict1:
#                     if keys != max1:
#                         prd *= dict1[keys]
#                 count += prd
#             dict1[i] += 1
#         return count
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
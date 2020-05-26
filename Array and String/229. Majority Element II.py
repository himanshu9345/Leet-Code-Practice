class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        c1, c2, c1count, c2count =  0, 0, 0, 0
        for i in nums:
            if c1 == i:
                c1count += 1
            elif c2 == i:
                c2count += 1
            elif c1count == 0:
                c1 = i
                c1count = 1
            elif c2count == 0:
                c2 = i
                c2count = 1
            else:
                c1count -= 1
                c2count -= 1
            # print i,c1,c2,c1count, c2count

        
        ans = []
        
        if nums.count(c1) > n/3:
            ans.append(c1)
        if c1!=c2 and nums.count(c2) > n/3:
            ans.append(c2)
        return ans
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
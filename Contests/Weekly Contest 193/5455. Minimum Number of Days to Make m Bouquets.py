class Solution(object):
    def fun1(self, day, arr, m, k):
        flower = 0
        for i in arr:
            if i <= day:
                flower += 1
                if flower == k:
                    m -= 1
                    # print i,m,"fff",day
                    flower = 0
                if m == 0:
                    return  True
            else:
                flower = 0
        return m == 0
    def minDays(self, bloomDay, m, k):
        l = 1
        r = 1000000000
        while l <= r:
            mid = l+((r-l)/2)
            if self.fun1(mid, bloomDay, m, k):
                r = mid - 1
            else:
                l = mid + 1
        # print l,r
        return l if self.fun1(l, bloomDay, m, k) else -1 
        
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        
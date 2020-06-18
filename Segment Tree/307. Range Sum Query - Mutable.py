    
class NumArray(object):

    def constructTree(self, si, arr, stL, stR):
        if stR<stL:
            return
        if stL == stR:
            # print si, stL
            self.ST[si] = arr[stL]
            return self.ST[si]

        mid = stL+ (stR-stL)/2
        # print stL,stR,mid,si

        self.ST[si] = self.constructTree(2*si + 1, arr, stL, mid) + self.constructTree(2*si + 2, arr, mid + 1, stR) 
        return self.ST[si]
        
    def getRange(self, si, ql, qr, stL, stR):
        # overlapping
        if stL >= ql and stR <= qr:
            return self.ST[si]
        #no overlapping
        if qr< stL or stR< ql:
            return 0
        #partial overlapping
        mid = (stL + stR)/2
        left = self.getRange(2*si+1, ql, qr, stL, mid)
        right = self.getRange(2*si+2, ql, qr, mid + 1, stR)
        # print left, right, stL,stR
        return left + right
    
    def updateTree(self, si, i, ql, qr, diff):
        if i < ql or i > qr:
            return 
        self.ST[si] += diff
        if ql!=qr:
            mid = (ql + qr)/2
            
            self.updateTree(2*si+1,i, ql, mid, diff) 
            self.updateTree(2*si+2, i, mid + 1, qr, diff)
    
    def __init__(self, nums):
        if nums:
            # h =2**int(math.ceil(math.sqrt((2*len(nums) - 1))))
            h = int(math.ceil(math.log(len(nums)+1,2)))
            self.ST = [0]*(4*len(nums))
            self.nums = nums
            # print self.ST
            self.constructTree(0, nums, 0, len(nums)-1)
        # print self.ST
        
        """
        :type nums: List[int]
        """
        

    def update(self, i, val):
        if not self.nums:
            return 
        diff = val - self.nums[i] 
        self.nums[i] = val
        self.updateTree(0, i, 0, len(self.nums)-1, diff )
        # print self.ST
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        

    def sumRange(self, i, j):
        if not self.nums:
            return  0
        return self.getRange(0, i, j, 0, len(self.nums)-1)
        
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
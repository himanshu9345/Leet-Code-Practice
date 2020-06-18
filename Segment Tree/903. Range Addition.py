n = 5
arr =[[1,  3,  2],
[2,  4,  3],
[0,  2, -2]]

    
class NumArray(object):

    # def constructTree(self, si, arr, stL, stR):
    #     if stR<stL:
    #         return
    #     if stL == stR:
    #         # print si, stL
    #         self.ST[si] = arr[stL]
    #         return self.ST[si]

    #     mid = stL+ (stR-stL)/2
    #     # print stL,stR,mid,si

    #     self.ST[si] = self.constructTree(2*si + 1, arr, stL, mid) + self.constructTree(2*si + 2, arr, mid + 1, stR) 
    #     return self.ST[si]
        
    def getRange(self, si, ql, qr, stL, stR):
        
        if ql>qr:
            return 
        if self.lazy[si]!=0:
            self.ST[si] = self.lazy[si]
            if ql!=qr:
                self.lazy[si*2+1] = self.lazy[si]
                self.lazy[si*2+2] = self.lazy[si]
            self.ST[si] =  0
        
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
    
    def updateTree(self, si, i, j, ql, qr, diff):
        if ql>qr:
            return 
        if self.lazy[si]!=0:
            self.ST[si] = self.lazy[si]
            if ql!=qr:
                self.lazy[si*2+1] = self.lazy[si]
                self.lazy[si*2+2] = self.lazy[si]
            self.lazy[si] =  0
        
        if j < ql or i > qr:
            return 
        if i<=ql and j>=qr:
            self.ST[si] = diff
            if ql!=qr:
                self.lazy[si*2+1] = diff
                self.lazy[si*2+2] = diff
            return
        
        mid = ql + (qr-ql)/2
            
        self.updateTree(2*si+1, i, j, ql, mid, diff) 
        self.updateTree(2*si+2, i, j , mid + 1, qr, diff)
        self.ST[si]= self.ST[si*2+1] +self.ST[si*2+2]
    
    # def __init__(self, nums):
    #     if nums:
    #         # h =2**int(math.ceil(math.sqrt((2*len(nums) - 1))))
    #         h = int(math.ceil(math.log(len(nums)+1,2)))
    #         self.ST = [0]*(4*len(nums))
    #         self.nums = nums
    #         # print self.ST
    #         self.constructTree(0, nums, 0, len(nums)-1)
    #     # print self.ST
        
    #     """
    #     :type nums: List[int]
    #     """
    def getModifiedArray(self, n, updates):
        if n:
            self.ST = [0] * (4*n)
            self.lazy = [0] * (4*n)
            self.arr = [0] * n
            for i, j, val in updates:
                # diff = val - self.arr[i]
                self.updateTree(0, i, j, 0, n-1, val)
                # self.arr[]
            print (self.ST)
            print (self.lazy)






    # def update(self, i, val):
    #     if not self.nums:
    #         return 
    #     diff = val - self.nums[i] 
    #     self.nums[i] = val
    #     self.updateTree(0, i, 0, len(self.nums)-1, diff )
    #     # print self.ST
    #     """
    #     :type i: int
    #     :type val: int
    #     :rtype: None
    #     """
        

    # def sumRange(self, i, j):
    #     if not self.nums:
    #         return  0
    #     return self.getRange(0, i, j, 0, len(self.nums)-1)
        
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
obj = NumArray()
obj.getModifiedArray(n,arr)
# param_2 = obj.sumRange(i,j)

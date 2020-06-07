class Solution(object):# recursive top to bottom
    def merge(self, list1, list2):
        left = 0
        right = 0
        res = []
        while left < len(list1) and right < len(list2):
            if list1[left] > list2[right]:
                res.append(list2[right])
                right += 1
            else:
                res.append(list1[left])
                left += 1
        
        res.extend(list1[left:])
        res.extend(list2[right:])
        return res
    
    def sortArray(self, nums):
        
        if len(nums) == 1:
            return nums
        mid = len(nums)/2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
class Solution(object):# iterative approach
    def merge(self, list1, list2):
        left = 0
        right = 0
        res = []
        while left < len(list1) and right < len(list2):
            if list1[left] > list2[right]:
                res.append(list2[right])
                right += 1
            else:
                res.append(list1[left])
                left += 1
        
        res.extend(list1[left:])
        res.extend(list2[right:])
        return res
    
    def sortArray(self, nums):
        
        
        if len(nums) == 1:
            return nums
        
        nums = [[i] for i in nums]
        while len(nums) != 1:
            res = []
            for i in range(len(nums)/2):
                res.append(self.merge(nums[2*i], nums[2*i+1]))
            if len(nums)%2 == 1:
                res.append(nums[-1])
            # print res
            nums = res
        return nums[0]
                    
            
#         mid = len(nums)/2
#         left = self.sortArray(nums[:mid])
#         right = self.sortArray(nums[mid:])
#         return self.merge(left, right)
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
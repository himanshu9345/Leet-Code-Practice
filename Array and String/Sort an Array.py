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
        
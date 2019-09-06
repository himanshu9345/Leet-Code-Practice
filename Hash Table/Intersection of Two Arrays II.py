class Solution(object):
    def intersect(self, nums1, nums2):
        dict1 = {}
        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1
        ans = []
        for i in nums2:
            if i in dict1:
                if dict1[i] > 0:
                    dict1[i] -= 1
                    ans.append(i)
        return ans
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

class Solution(object):
    def maxSumDivThree(self, nums):
        dict1 = {}
        sum1 = sum(nums)
        for i in nums:
            g = i % 3
            if g in dict1:
                dict1[g].append(i)
            else:
                dict1[g] = [i]
        if 1 in dict1:
            dict1[1] = sorted(dict1[1], reverse=True)

        if 2 in dict1:
            dict1[2] = sorted(dict1[2], reverse=True)

        rem = sum1 % 3
        if rem == 0:
            return sum1

        if rem == 1:
            if rem in dict1:
                max1 = dict1[rem].pop()
                max2 = 1000000000
                if 2 in dict1 and len(dict1[2]) > 1:
                    max1 = dict1[2].pop() + dict1[2].pop()
                return sum1 - min(max1, max2)
            else:
                sum1 -= dict1[2].pop() + dict1[2].pop()
                return sum1
        else:
            if rem in dict1:
                max1 = dict1[2].pop()
                max2 = 1000000000
                if 1 in dict1 and len(dict1[1]) > 1:
                    max2 = dict1[1].pop() + dict1[1].pop()
                return sum1 - min(max1, max2)
            else:
                sum1 -= dict1[1].pop() + dict1[1].pop()
                return sum1

        """
        :type nums: List[int]
        :rtype: int
        """

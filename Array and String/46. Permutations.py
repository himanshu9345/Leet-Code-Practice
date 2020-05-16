class Solution(object):
    def permute(self, nums):

        seen = set()
        ans = []

        def bt(arr, seen, ans, nums):
            for i in nums:
                if i not in seen:
                    arr.append(i)

                    seen.add(i)
                    if len(arr) == len(nums):
                        ans.append(arr[:])
                        # print arr
                    else:
                        bt(arr, seen, ans, nums)
                    seen.remove(i)
                    arr.pop()

        bt([], seen, ans, nums)
        return ans

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

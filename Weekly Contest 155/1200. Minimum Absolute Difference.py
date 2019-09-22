class Solution(object):
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        min1 = 1000000
        dict1 = {}
        for i in range(len(arr) - 1):
            min1 = min(min1, arr[i + 1] - arr[i])
            if arr[i + 1] - arr[i] in dict1:
                dict1[arr[i + 1] - arr[i]].append([arr[i], arr[i + 1]])
            else:
                dict1[arr[i + 1] - arr[i]] = [[arr[i], arr[i + 1]]]
        # print min1
        return dict1[min1]
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

class Solution(object):
    def findRestaurant(self, list1, list2):
        dict1 = {}
        for index, value in enumerate(list1):
            dict1[value] = index
        dict2 = {}
        for index, value in enumerate(list2):
            dict2[value] = index
        common = list(set(list1).intersection(set(list2)))
        # printcommon
        min1 = 100000
        rest = []
        for i in common:
            # print i
            sum1 = dict1[i] + dict2[i]
            if sum1 < min1:
                min1 = sum1
                rest = [i]
            elif sum1 == min1:
                rest.append(i)
        return rest

        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

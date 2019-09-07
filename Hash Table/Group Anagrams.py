class Solution(object):
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in strs:
            # print i
            newi = sorted(i)
            newi = "".join(newi)
            if newi in dict1:
                dict1[newi].append(i)
            else:
                dict1[newi] = [i]
        return dict1.values()
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

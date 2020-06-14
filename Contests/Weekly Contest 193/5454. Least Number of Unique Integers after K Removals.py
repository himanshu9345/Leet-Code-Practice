class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        c = Counter(arr)
        sorted_c = sorted(c,key = c.get)
        i = 0
        while i < len(sorted_c) and k>0:
            c_count = c[sorted_c[i]]
            if c_count>k:
                break
            elif c_count == k:
                del c[sorted_c[i]]
                break
            else:
                k -= c[sorted_c[i]]
            del c[sorted_c[i]]
            # print c
            i += 1

        return len(c)     
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
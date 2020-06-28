class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = defaultdict(int)
        for i in arr:
            dict1[i%k]+=1
        # print dict1
        
        for i in range(1, k):
            # print i
            if i!=k-i and dict1[i] == dict1[k-i]:
                continue
            elif i == (k-i):
                if dict1[i]%2:
                    return False
            else:
                return False
        return True
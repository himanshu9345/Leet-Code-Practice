class Solution(object):
    def fourSumCount(self, A, B, C, D):
        count = 0

        ans = []
        for i in A:
            for j in B:
                ans.append(i + j)

        ans1 = []
        for i in C:
            for j in D:
                ans1.append(i + j)

        dict1 = {}
        for i, k in enumerate(ans1):
            dict1[k] = dict1.get(k, 0) + 1

        for i in ans:
            if -i in dict1:
                count += dict1[-i]
        return count

        """
        x = collections.defaultdict(int)
        for a in A:
            for b in B:
                x[a+b] +=1
        result = 0
        for c in C:
            for d in D:
                if -(c+d) in x:
                    result += x[-(c+d)]
        return result
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

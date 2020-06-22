class Solution(object):
    def getFolderNames(self, names):
        seen = set()
        dict1 =defaultdict(int)
        ans = []
        for i in names:
            if i in dict1:
                str1 = i
                while i in seen:
                    i = str1+"("+str(dict1[str1])+")"
                    dict1[str1] += 1
                ans.append(i)
                seen.add(i)
                dict1[i] += 1
                # print seen, i, str1
            else:
                dict1[i] += 1
                seen.add(i)
                ans.append(i)
            # print dict1,seen
        return ans
        """
        :type names: List[str]
        :rtype: List[str]
        """
        
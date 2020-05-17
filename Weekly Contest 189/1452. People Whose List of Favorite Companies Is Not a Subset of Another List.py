class Solution:
    def peopleIndexes(self, a1: List[List[str]]) -> List[int]:
        dict1 = {}
        for i,v in enumerate(a1):
            for j in v:
                if j in dict1:
                    dict1[j].append(i)
                else:
                    dict1[j] = [i]
        ans = []
        for i in a1:
            seen = set(dict1[i[0]])
            for j in i:
                seen = seen.intersection(set(dict1[j]))
            # print (seen)
            if len(seen)==1:
                ans+=list(seen)
        return ans

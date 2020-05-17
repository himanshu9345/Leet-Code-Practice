from collections import Counter
class Solution(object):
    # smoothly adding and removing element from dict
    def dictAdd(self, dict1, a):
        if a in dict1:
            dict1[a] += 1
        else:
            dict1[a] = 1
    def dictRemove(self, dict1, a):
        if dict1[a] == 1:
            del dict1[a]
        else:
            dict1[a] -= 1
    
    def findAnagrams(self, s, p):
        dict1 = dict(Counter(p))
        
        # read p length of char from s
        comp = dict(Counter(s[:len(p)]))
        ans = []
        if comp == dict1:
            ans.append(0)
        
        start = 0
        for i in range(len(p),len(s)):
            self.dictRemove(comp, s[start])
            start += 1
            self.dictAdd(comp, s[i])
            if comp == dict1:
                ans.append(start)
        
        return ans
        
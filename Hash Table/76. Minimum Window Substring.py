class Solution(object):
    def minWindow(self, s, t):
        dictt = Counter(t)
        filtered_s = [(v,i) for i, v in enumerate(s) if v in dictt]
        arr = defaultdict(int)
        min1 = float('inf')
        minindex = (0,0)
        formed = 0
        
        n = len(filtered_s)
        i, j = 0, 0
        while j < n:
            char = filtered_s[j][0]
            arr[char] += 1
            # sub str char is formed when that charcter occors samenumber of  time additional wont be counter towards formed
            if char in dictt and arr[char] == dictt[char] :
                formed += 1
            while formed == len(dictt) and j>=i:
                char = filtered_s[i][0]
                end = filtered_s[j][1]
                start = filtered_s[i][1]
                if min1 > end - start + 1:
                    minindex = (start, end)
                    min1 = end - start + 1 
                arr[char] -= 1
                if char in dictt and dictt[char] > arr[char]:
                    formed -=1
                i += 1
            j += 1
        if min1 == float('inf'):
            return ""
        return s[minindex[0]:minindex[1]+1]
            
        """
        :type s: str
        :type t: str
        :rtype: str

        """
# only care about charcters that are in T
# best approach to solve sliding windows problems so far
class Solution(object):
    # def compare1(self, d1, d2):
    #     for key in d1:
    #         if key not in d2 or d1[key] > d2[key]:
    #             return False
    #     return True
    def minWindow(self, s, t):
        dictt = Counter(t)
        # filtered_s = [(v,i) for i, v in enumerate(s) if v in dictt]
        # print filtered_s
        arr = defaultdict(int)
#         match = defaultdict(int)
        
#         for i in t:
#             match[ord(i) - 65]+=1
        min1 = float('inf')
        minindex = (0,0)
        formed = 0
        
        n = len(s)
        i, j = 0, 0
        while j < n:
            arr[s[j]] += 1
            if s[j] in dictt and arr[s[j]] == dictt[s[j]] :
                formed += 1
            while formed == len(dictt) and j>=i:
                # print j,i,min1, formed
                if min1 > j-i +1:
                    minindex = (i,j)
                    min1 = j - i+1
                arr[s[i]] -= 1
                if s[i] in dictt and dictt[s[i]] > arr[s[i]]:
                    formed -=1
                # print formed,s[i]
                i += 1
            # print arr, dictt, formed
            j += 1
#             while self.compare1(match,arr) and  i < n and i <= j:
#                 
#                 arr[ord(s[i]) - 65] -= 1
#                 i +=1
#             j += 1
        # print minindex 
        if min1 == float('inf'):
            return ""
        return s[minindex[0]:minindex[1]+1]
            


# My approach 
class Solution(object):
    def compare1(self, d1, d2):
        for key in d1:
            if key not in d2 or d1[key] > d2[key]:
                return False
        return True
    def minWindow(self, s, t):
        arr = defaultdict(int)
        match = defaultdict(int)
        
        for i in t:
            match[ord(i) - 65]+=1
        min1 = float('inf')
        minindex = (0,0)
        n = len(s)
        i, j = 0, 0
        while j < n:
            # while not self.compare1(match,arr) and j < n :
            #     arr[ord(s[j]) - 65] += 1
            #     j += 1
            # print arr, match,i,j,min1
            arr[ord(s[j]) - 65] += 1
            while self.compare1(match,arr) and  i < n and i <= j:
                if min1 > j-i:
                    minindex = (i,j+1)
                    min1 = j - i
                arr[ord(s[i]) - 65] -= 1
                i +=1
            j += 1

                
            # if j - i<=len(t):
            #     if min1 > j-i:
            #         minindex = (i,j)
            #         min1 = j - i
            #     break
        # print minindex
        return s[minindex[0]:minindex[1]]

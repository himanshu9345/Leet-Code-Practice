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
        
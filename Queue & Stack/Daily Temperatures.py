class Solution(object):#TLE
    def dailyTemperatures(self, T):
        ans = [0]
        news = [T.pop()]
        while T:
            if T[-1] < news[-1]:
                ans.append(1)
            elif len(news) > 1:
                count = 0
                for i in range(len(news) - 2, -1, -1):
                    if news[i] > T[-1]:
                        ans.append(len(news) - i)
                        break
                if len(ans) == len(news):
                    ans.append(0)
            else:
                ans.append(0)
            news.append(T.pop())
        return ans[::-1]

        """
        :type T: List[int]
        :rtype: List[int]
        """

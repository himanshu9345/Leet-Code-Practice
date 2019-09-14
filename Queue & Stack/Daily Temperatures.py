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

class Solution1(object):#Accepted
    def dailyTemperatures(self, T):
        temp = [30001] * 101
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            min1 = 30001
            for j in range(T[i] + 1, 101):
                min1 = min(min1, temp[j])
            if min1 == 30001:
                ans[i] = 0
            else:
                ans[i] = min1 - i
            temp[T[i]] = i
        return ans

        """
        :type T: List[int]
        :rtype: List[int]
        """


class Solution2(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
            if stack:
                # print stack
                ans[i] = stack[-1][1] - i

            stack.append((T[i], i))
        return ans

        """
        :type T: List[int]
        :rtype: List[int]
        """

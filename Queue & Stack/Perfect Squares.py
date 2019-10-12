def bfs(n):
    queue = [n]
    count = 0
    while queue:
        seen = set()
        count += 1
        for i in range(len(queue)):
            num = queue[i]
            if num == 0:
                return count - 1
            for i in range(1, int(math.sqrt(num)) + 1):
                diff = num - i ** 2
                if diff >= 0 and diff not in seen:
                    seen.add(diff)
        queue = list(seen)


class Solution(object):
    def numSquares(self, n):
        return bfs(n)
        """
        :type n: int
        :rtype: int
        """

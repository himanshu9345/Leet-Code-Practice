from collections import deque


def bfs(grid, m, n, q, seen, i, j):
    r, c = [1, -1, 0, 0], [0, 0, 1, -1]
    q.append((i, j))
    while (q):
        for i in range(len(q)):

            x, y = q.pop()
            # print x,y
            for i in range(4):
                mx, ny = x + r[i], y + c[i]
                if mx >= 0 and mx < m and ny >= 0 and ny < n and (mx, ny) not in seen and grid[mx][ny] == "1":
                    q.append((mx, ny))
                    seen.add((mx, ny))


class Solution(object):
    def numIslands(self, grid):
        if grid == []:
            return 0
        seen = set()
        q = deque()
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                # print grid[i][j],seen
                if (i, j) not in seen and grid[i][j] == "1":
                    seen.add((i, j))
                    bfs(grid, m, n, q, seen, i, j)
                    count += 1
        return count

        """
        :type grid: List[List[str]]
        :rtype: int
        """

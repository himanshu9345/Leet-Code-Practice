class Solution(object):
    def shiftGrid(self, grid, k):

        m = len(grid)
        n = len(grid[0])
        ans = []
        for i in range(m):
            for j in range(n):
                ans.append(grid[i][j])
        if k > len(ans) and len(ans) != 0:
            k = k % len(ans)
        ans = ans[-k:] + ans[:-k]
        k = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = ans[k]
                k += 1
        return grid
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

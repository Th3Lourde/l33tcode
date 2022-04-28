from collections import deque

class Solution:
    def largestIsland(self, grid):
        N = len(grid)

        def traverse(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j


        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in traverse(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        index = 2
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in traverse(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)

        return res

[
[0,1,0],
[1,0,1],
[1,0,0],
]

print(Solution().largestIsland([[0,1,0],[1,0,1],[1,0,0]]))

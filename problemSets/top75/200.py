'''
Number of islands problem, perform a dfs/bfs on every one and set all
adjacent lands to zero to avoid double counting, have a counter to count the island
'''

from collections import deque

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def traverse(r,c):
            q = deque([(r,c)])

            while q:
                r,c = q.pop()

                if grid[r][c] == "1":
                    grid[r][c] = "0"

                    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "1":
                                q.appendleft((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    traverse(r,c)

        return islands

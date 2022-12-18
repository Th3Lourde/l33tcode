from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        numHealthy = 0
        q = deque()
        itr = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    numHealthy += 1

                elif grid[r][c] == 2:
                    q.appendleft((r,c))

        if numHealthy == 0:
            return 0

        while len(q) > 0:
            newQ = deque()
            itr += 1

            while q:
                r,c = q.pop()

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            numHealthy -= 1
                            grid[nr][nc] = 2
                            newQ.appendleft((nr,nc))

            q = newQ

        if numHealthy != 0:
            return -1

        return itr-1

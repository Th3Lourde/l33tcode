from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)
        neibs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        if grid[0][0] == 1:
            return -1

        seen = set()

        q = deque([(1,0,0)])

        while q:
            dist,r,c = q.pop()

            if r == N-1 and c == N-1:
                return dist


            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r+1, c-1), (r-1, c-1), (r-1, c+1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and (nr,nc) not in seen:
                        seen.add((r,c))
                        q.appendleft((dist+1, nr, nc))

        return -1

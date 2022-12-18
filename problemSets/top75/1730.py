from collections import deque

# what if we reverse it?
# what if the food looks for the starting location?
# sounds good, let's do that
'''
[["X","X","X","X","X"],
 ["X","*","X","O","X"],
 ["X","O","X","#","X"],
 ["X","X","X","X","X"]]

 q []
 seen (2,3), (1,3)
 2
 nq []

(1,3)


'''
class Solution:
    def getFood(self, grid):
        # 1) Find starting point
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "#":
                    q.appendleft((r,c))
                    seen.add((r,c))

        dist = 0

        while q:
            newQ = deque()

            while q:
                r,c = q.pop()

                if grid[r][c] == "*":
                    return dist

                for nr, nc in [(r+1,c), (r-1,c), (r, c+1), (r,c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                        if grid[nr][nc] != "X":
                            seen.add((nr,nc))
                            newQ.appendleft((nr,nc))

            dist += 1
            q = newQ

        return -1

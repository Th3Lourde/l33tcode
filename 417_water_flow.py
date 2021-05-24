'''
Ok so I was thinking about it wrong.

I was thinking that we care about squares
that can reach both sides.

We do care about that, however we can just
start from all pacific squares and see all of
the water that can be reached from these squares.

Do the same with atlantic.

Then coordinates that can be reached by both are
included in our answer.
'''
from collections import deque
class Solution:
    # Correct, too slow, add cache?
    def pacificAtlantic_1(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        canReach = []

        def bfs(row,column):
            q = deque()
            q.append((row,column))
            seen = set()

            canReachPacific = False
            canReachAtlantic = False

            while q and (canReachPacific == False or canReachAtlantic == False):
                r, c = q.popleft()
                seen.add((r,c))

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if nr < 0 or nc < 0:
                        canReachPacific = True
                    elif nr >= rows or nc >= cols:
                        canReachAtlantic = True
                    elif (nr,nc) not in seen and matrix[r][c] >= matrix[nr][nc]:
                        q.append((nr,nc))

            return canReachAtlantic and canReachPacific

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if bfs(r,c):
                    canReach.append([row, column])

        return canReach

    def pacificAtlantic(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        pacific = deque([[r,0] for r in range(rows)] + [[0,c] for c in range(1, cols)])

        atlantic = deque([[rows-1, c] for c in range(cols)] + [[r,cols-1] for r in range(rows-1)])

        # print(pacific)
        # print(atlantic)

        def bfs(queue):
            seen = set()

            while queue:
                r,c = queue.popleft()

                seen.add((r,c))

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if matrix[r][c] <= matrix[nr][nc]:
                            if (nr, nc) not in seen:
                                queue.append((nr, nc))

            return seen

        landBothOceansCanReach = []

        landPacificCanReach  = bfs(pacific)
        landAtlanticCanReach = bfs(atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in landPacificCanReach and (r,c) in landAtlanticCanReach:
                    landBothOceansCanReach.append([r,c])

        return landBothOceansCanReach

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

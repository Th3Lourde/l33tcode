from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        pacific = []
        atlantic = []

        rows = len(heights)
        cols = len(heights[0])

        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))

        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1, c))

        def bfs(land):
            canReach = set()

            for r,c in land:
                q = deque([(r,c)])

                while q:
                    r,c = q.pop()

                    canReach.add((r,c))

                    for nr, nc in [(r+1,c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if heights[r][c] <= heights[nr][nc] and (nr,nc) not in canReach:
                                canReach.add((nr,nc))
                                q.appendleft((nr,nc))

            return canReach


        return list(bfs(pacific) & bfs(atlantic))





print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        target = (len(grid)-1, len(grid[0])-1)
        q = deque([(0,0,1)])
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        if grid[0][0] != 0:
            return -1

        while len(q) > 0:
            x,y,count = q.pop()

            if (x,y) == target:
                return count

            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]:
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 0 and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.appendleft((nx,ny,count+1))

        return -1

print(Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))

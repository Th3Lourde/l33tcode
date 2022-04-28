from collections import deque
class Solution:
    def shortestPath(self, grid, k):
        if grid[0][0] == 1:
            k -= 1

        q = deque({(0,0,k,0)})
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        while q:
            row, col, kLeft, steps = q.pop()

            seenTuple = (row, col, kLeft)

            if seenTuple in seen:
                continue

            seen.add((row, col, kLeft))

            if row == rows-1 and col == cols-1:
                return steps

            for nRow, nCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= nRow < rows and 0 <= nCol < cols:
                    if grid[nRow][nCol] == 1 and kLeft > 0:
                        q.appendleft((nRow, nCol, kLeft-1, steps+1))

                    elif grid[nRow][nCol] == 0:
                        q.appendleft((nRow, nCol, kLeft, steps+1))

        return -1

print(Solution().shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))
print(Solution().shortestPath([[0,1,1],[1,1,1],[1,0,0]], 2))

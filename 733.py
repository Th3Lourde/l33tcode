'''
Given sr, sc (row, column),
set image[sr][sc] to newColor,
as well as all cells that have
that color that can be touched
bfs.

0(n)

'''

from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        target_color = image[sr][sc]

        def dfs(r,c):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == target_color:
                        image[nr][nc] = newColor
                        dfs(nr,nc)

        image[sr][sc] = newColor
        dfs(sr, sc)
        return image


print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))

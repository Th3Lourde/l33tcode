'''
You are given an n x n integer matrix
where each value grid[i][j] represents a height

I think that it is missing a paragraph that says:
You can swim into higher water. If you


[
[0,5,6],
[1,7,2],
[8,3,4],
]

[[0,5,6], [1,2,7], [8,3,4]]

Ok so find a path from the top left to the bottom
right such that the max element in the path is minimized

We can brute force this by following all paths.

Or we can proceed with the min paths first, with a dijkstra-like traversal
of the grid, where we only move forward with the smallest path

[
(1)
(24)
(23)
]
'''

import heapq

class Solution:
    def swimInWater(self, grid):
        heap = [(grid[0][0],0,0)]
        t = len(grid)-1
        seen = set({(0,0)})

        while heap:
            maxTerm, r, c = heapq.heappop(heap)

            if r == t and c == t:
                return maxTerm

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr <= t and 0 <= nc <= t and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(heap, (max(maxTerm, grid[nr][nc]), nr, nc))

            grid[r][c] = -1

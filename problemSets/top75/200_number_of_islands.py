'''
Every time we see a 1, perform a bfs
and set every touchable 1 to a zero.
'''
class Solution:
    def numIslands(self, grid):
        numOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def dfs(stack):
            # print(queue)
            while stack:
                r,c = stack.pop()
                seen.add((r,c))

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in seen:
                            if grid[nr][nc] == "1":
                                stack.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    numOfIslands += 1
                    dfs([[r,c]])

        return numOfIslands

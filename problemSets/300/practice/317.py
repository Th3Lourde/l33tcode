from collections import deque

class Solution:
    def shortestDistance(self, grid):
        houses = []
        c_to_d = {}
        rows = len(grid)
        cols = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    c_to_d[(row,col)] = 0

                elif grid[row][col] == 1:
                    houses.append((row,col))


        def bfs(row, col, c_t_d):
            distance = 0
            visited = set()
            q = [(row, col)]

            while q:
                distance += 1
                next_level = []

                for r,c in q:
                    for nR, nC in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0 <= nR < rows and 0 <= nC < cols:
                            if (nR, nC) not in visited:
                                if (nR, nC) in c_t_d:
                                    c_t_d[(nR,nC)] += distance
                                    visited.add((nR, nC))
                                    next_level.append((nR, nC))

                q = next_level

            if len(visited) != len(c_t_d):
                lands_to_remove = set(c_t_d.keys()).difference(visited)

                for land in lands_to_remove:
                    c_t_d.pop(land)


        for r,c in houses:
            bfs(r, c, c_to_d)

        # print(houses)
        # print(c_to_d)

        if len(houses) > 0 and len(c_to_d) > 0:
            vals = list(c_to_d.values())
            return min(vals)

        return -1


    def shortestDistance_1(self, grid):
        ans = float('inf')
        rows = len(grid)
        cols = len(grid[0])
        cache = {}

        # First find the ones
        ones = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    ones.append((row,col))

        def bfs(row, col, targetRow, targetCol):
            q = deque([(row, col, set())])

            if (row, col, targetRow, targetCol) in cache:
                return cache[(row, col, targetRow, targetCol)]

            while q:
                row, col, seen = q.pop()

                if row == targetRow and col == targetCol:
                    cache[(row, col, targetRow, targetCol)] = len(seen)
                    return len(seen)

                seen.add((row,col))

                if grid[row][col] == 1:
                    continue

                for nr, nc in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr,nc) not in seen and grid[nr][nc] != 2:
                            q.appendleft((nr, nc, set(seen)))

            return float('inf')

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 0:
                    distance = 0

                    for tRow, tCol in ones:
                        distance += bfs(row, col, tRow, tCol)

                        if distance > ans:
                            break


                    ans = min(ans, distance)

        if ans == float('inf'):
            return -1

        return ans

print(Solution().shortestDistance([[1,0]]))
print(Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))

print(Solution().shortestDistance([[2,0,2,0,0,1,0,0,2,0,2,0,0,2,2,0,1,0,0,0,0,2,0,2,0,2,2,2,0,0,0,0,2,0,2,0,0,2,2],[2,0,0,2,2,2,0,0,0,0,2,2,2,0,2,2,0,0,0,0,0,0,0,2,0,2,2,2,2,0,1,0,2,2,2,0,0,2,0],[0,0,0,2,2,0,2,2,2,0,0,0,2,0,1,0,0,2,2,2,0,2,0,2,1,2,2,2,0,2,2,0,0,2,0,0,0,0,0],[0,0,0,2,2,2,2,0,2,0,0,0,1,0,2,0,0,2,0,0,1,2,0,0,0,2,2,1,0,0,0,0,0,2,2,0,0,2,1],[0,0,0,0,0,0,0,0,0,2,2,2,0,2,2,0,0,0,0,2,1,0,0,0,0,0,2,0,2,0,2,0,0,0,0,2,2,2,0],[0,0,0,1,2,2,2,0,0,0,2,1,0,0,2,0,0,2,0,0,0,0,0,0,2,0,2,0,2,2,2,0,2,1,0,0,2,2,0],[0,2,2,2,0,0,0,0,2,0,2,2,0,2,0,2,1,2,2,2,2,0,0,2,0,2,2,0,0,0,2,0,0,2,2,0,0,2,0]]))

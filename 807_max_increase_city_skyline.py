

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        rowSky = [-1 for _ in range(len(grid))]
        colSky = [-1 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > rowSky[i]:
                    rowSky[i] = grid[i][j]

                if grid[i][j] > colSky[j]:
                    colSky[j] = grid[i][j]

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff = min(rowSky[i], colSky[j]) - grid[i][j]

                if diff > 0: ans += diff

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

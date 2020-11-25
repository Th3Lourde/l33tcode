
class Solution:

    def isValid(self, row, col):
        return 0 <= row <= self.maxRow and 0 <= col <= self.maxCol and self.grid[row][col] == 1

    def itr(self, row, col, uid):
        self.grid[row][col] = uid
        self.d[uid] += 1

        if self.isValid(row+1, col):
            self.itr(row+1, col, uid)
        if self.isValid(row-1, col):
            self.itr(row-1, col, uid)
        if self.isValid(row, col+1):
            self.itr(row, col+1, uid)
        if self.isValid(row, col-1):
            self.itr(row, col-1, uid)

    def maxAreaOfIsland(self, grid):
        self.maxRow = len(grid)-1
        self.maxCol = len(grid[0])-1
        self.grid = grid
        ans = 0
        self.d = {}
        uid = 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    uid += 1
                    self.d[uid] = 0
                    self.itr(row, col, uid)
                    ans = max(ans, self.d[uid])

        return ans


if __name__ == '__main__':
    s = Solution()

    m = [[0,0,0,0,0,0,0,0]]
    print(s.maxAreaOfIsland(m))



class Solution:
    def minPathSum(self, grid):

        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]

        cpy = []

        # create blank slate
        for i in range(len(grid)):
            cpy.append([0]*len(grid[0]))


        # fill out top
        for i in range(len(grid[0])):
            if i == 0:
                cpy[0][i] = grid[0][i]

            elif i != 0:
                cpy[0][i] = cpy[0][i-1] + grid[0][i]


        # fill out left most column
        for j in range(1, len(grid)):
            cpy[j][0] = cpy[j-1][0] + grid[j][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                cpy[i][j] = min(cpy[i][j-1], cpy[i-1][j]) + grid[i][j]



        return cpy[-1][-1]


if __name__ == '__main__':
    s = Solution()
    # m = [ [1,3,1], [1,5,1], [4,2,1] ]
    m = [[1,2,5],[3,2,1]]
    print(s.minPathSum(m))

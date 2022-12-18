'''
X-matrix if both;
1) all elements in the diags are non-zero
2) all elements not in diags are zero

So what is a Diag?

I'm assuming you start from the top left and go to the bottom right
'''

class Solution:
    def checkXMatrix(self, grid):
        visited = set()

        # check top left diag
        for i in range(len(grid)):
            visited.add((i,i))
            if grid[i][i] == 0:
                return False

        r,c = len(grid)-1, 0

        while r >= 0 and c < len(grid):
            visited.add((r,c))
            if grid[r][c] == 0:
                return False

            r -= 1
            c += 1


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited:
                    if grid[r][c] != 0:
                        return False

        return True

print(Solution().checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
print(Solution().checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]))

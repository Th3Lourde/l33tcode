'''
Given an m x n binary matrix filled with 0's and 1'
find the largest square containing only 1's and return it's
area

So start from top left, go to bottom right, for every
cell that is a 1, start expanding and see what you get.

Have a max area variable that we keep updating

So there is a dp solution here, not sure what it is.
That's ok. We can learn. I'd say our current algo
is 0(n^2).


'''

class Solution:
    def maximalSquare(self, matrix):
        cache = {}
        rows = len(matrix)
        cols = len(matrix[0])
        maxSquare = 0

        def dp(i,j):
            if (i,j) in cache:
                return cache[(i,j)]

            if matrix[i][j] == "0":
                return 0

            if i < 0 or j < 0:
                return 0


            cache[(i,j)] = min(dp(i-1,j), dp(i,j-1), dp(i-1, j-1))+1

            return cache[(i,j)]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    maxSquare = max(maxSquare, dp(r,c))

        return maxSquare*maxSquare



print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]))

print(Solution().maximalSquare([["0"]]))

print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]]))

print(Solution().maximalSquare([["0","1"],["1","0"]]))

'''
Given two arrays: row sum, col sum.

rowSum[i] is the sum of the elements in the ith row
colSum[j] is the sum of the elements in the jth column

Find any matrix composed of non-negative integers of proper
size that satisfies the requirements. It is given that at
least one matrix that fulfills the requirements exists.

Hmm it's a bunch of algebra problems

Pretty sure brute-force is the way to go here. Question
is what to brute force.

Idea: start at top-left corner, loop through all possible
values, (stop when sum is too large), every time we find
something that fits, move on to the next corner.

So recursive calls with backtracking.
Base condition: if we hit bottom right corner:
1) Find valid solution: then return the matrix

How to brute-force the values: Loop through all possible
values in the corner, option to += 1 to value or to not.
'''

class Solution:
    def restoreMatrix(self, rowSum, colSum):
        n = len(rowSum)
        m = len(colSum)

        matrix = [[0 for _ in range(m)] for _ in range(n)]

        for row in range(n):
            for col in range(m):
                matrix[row][col] = min(rowSum[row], colSum[col])

                rowSum[row] -= matrix[row][col]
                colSum[col] -= matrix[row][col]

        return matrix

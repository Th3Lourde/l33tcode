'''
[1,1,1]
[1,0,1]
[1,1,1]
'''

class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        def setToZero(r,c):
            for row in range(rows):
                matrix[row][c] = 0

            for col in range(cols):
                matrix[r][col] = 0

        zeroes = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroes.append((r,c))

        for r,c in zeroes:
            setToZero(r,c)

        for row in matrix:
            print(row)

print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

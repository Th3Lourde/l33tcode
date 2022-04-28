'''
for every position in
'''


class Solution:
    def isToeplitzMatrix(self, matrix):

        def isToeplitz(r,c):
            term = matrix[r][c]

            r += 1
            c += 1

            while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                if matrix[r][c] != term:
                    return False

                r += 1
                c += 1

            return True

            
        for row in range(len(matrix)):
            if not isToeplitz(row, 0):
                return False

        for col in range(1, len(matrix[0])):
            if not isToeplitz(0, col):
                return False

        return True

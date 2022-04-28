class Solution:
    def isToeplitzMatrix(self, matrix):
        # Traverse matrix, check if
        # matrix[row][col] == matrix[row-1][col-1]
        rows = len(matrix)
        cols = len(matrix[0])

        for row_idx in range(1, rows):
            for col_idx in range(1, cols):
                if matrix[row_idx][col_idx] != matrix[row_idx-1][col_idx-1]:
                    return False

        return True

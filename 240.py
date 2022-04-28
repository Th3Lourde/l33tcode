class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        row, col = 0, len(matrix[0])-1

        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False

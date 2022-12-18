'''
Given a matrix, return all elements in spiral order.

colMin = 1
colMax = 1
rowMin = 1
rowMax = 1

loop through top
loop through side
loop though

'''

class Solution:
    def spiralOrder(self, matrix):
        rowMin = 0
        rowMax = len(matrix)

        colMin = 0
        colMax = len(matrix[0])

        traversal = []

        while rowMin < rowMax and colMin < colMax:
            # Add in checks to return when we run out of room

            # Iterate top
            for c in range(colMin, colMax):
                traversal.append(matrix[rowMin][c])

            rowMin += 1

            if not(rowMin < rowMax and colMin < colMax):
                break

            # Iterate rhs
            for r in range(rowMin, rowMax):
                traversal.append(matrix[r][colMax-1])

            colMax -= 1

            if not(rowMin < rowMax and colMin < colMax):
                break

            # Iterate bottom
            for c in range(colMax-1, colMin-1, -1):
                traversal.append(matrix[rowMax-1][c])

            rowMax -= 1

            if not(rowMin < rowMax and colMin < colMax):
                break

            # Iterate left
            for r in range(rowMax-1, rowMin-1, -1):
                traversal.append(matrix[r][colMin])

            colMin += 1

        return traversal

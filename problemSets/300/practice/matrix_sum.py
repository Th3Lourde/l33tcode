class NumMatrix:
    def __init__(self, matrix):
        col = [0]*len(matrix[0])
        self.matrixSum = []
        self.matrix = matrix

        for _ in range(len(matrix)):
            self.matrixSum.append(list(col))

        # Calculate rows
        rowSum = 0
        for row in range(len(matrix)):
            rowSum += matrix[row][0]
            self.matrixSum[row][0] = rowSum

        # Calculate cols
        colSum = 0
        for col in range(len(matrix[0])):
            colSum += matrix[0][col]
            self.matrixSum[0][col] = colSum

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                self.matrixSum[row][col] = matrix[row][col] + self.matrixSum[row][col-1] + self.matrixSum[row-1][col] - self.matrixSum[row-1][col-1]

        def calculate_sum(matrix, r, c):
            resp = 0

            for row in range(r+1):
                for col in range(c+1):
                    resp += matrix[row][col]

            return resp

    def sumRegion(self, row1, col1, row2, col2):
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]

        if row1 == 0 and col1 == 0:
            return self.matrixSum[row2][col2]

        resp = self.matrixSum[row2][col2]

        if row1 > 0:
            resp -= self.matrixSum[row1-1][col2]

        if col1 > 0:
            resp -= self.matrixSum[row2][col1-1]

        if row1 > 0 and col1 > 0:
            resp += self.matrixSum[row1-1][col1-1]

        return resp

["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[8,-4,5],[-1,4,4],[-2,3,1],[-4,4,3]]],[0,1,0,2],[1,1,1,2],[0,1,0,2]]

m = NumMatrix([[8,-4,5],[-1,4,4],[-2,3,1],[-4,4,3]])
m.sumRegion(0,1,0,2)


# m = NumMatrix([[-4,-5]])
#
# m.sumRegion(0,0,0,0)
# m.sumRegion(0,0,0,1)
# m.sumRegion(0,1,0,1)
#
#
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]


# m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# m.sumRegion(2, 1, 4, 3)
# m.sumRegion(1, 1, 2, 2)
# m.sumRegion(1, 2, 2, 4)

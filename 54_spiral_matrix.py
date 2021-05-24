class Solution:
    def spiralOrder(self, m):
        path = []

        minRow = 0
        maxRow = len(m)

        minCol = 0
        maxCol = len(m[0])

        while minRow < maxRow and minCol < maxCol:

            # Top:
            for col in range(minCol, maxCol):
                path.append(m[minRow][col])

            minRow += 1

            if not (minRow < maxRow and minCol < maxCol):
                break

            # Right:
            for row in range(minRow, maxRow):
                path.append(m[row][maxCol-1])

            maxCol -= 1

            if not (minRow < maxRow and minCol < maxCol):
                break

            # Bottom:
            for col in range(maxCol-1, minCol-1, -1):
                path.append(m[maxRow-1][col])

            maxRow -= 1

            if not (minRow < maxRow and minCol < maxCol):
                break

            # Left:
            for row in range(maxRow-1, minRow-1, -1):
                path.append(m[row][minCol])

            minCol += 1

            if not (minRow < maxRow and minCol < maxCol):
                break

        return path

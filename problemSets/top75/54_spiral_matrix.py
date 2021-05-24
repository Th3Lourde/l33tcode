class Solution:
    def spiralOrder(self, matrix):
        rMin, cMin = 0,0
        rMax, cMax = len(matrix), len(matrix[0])

        order = []

        while rMin < rMax and cMin < cMax:
            # Top
            for c in range(cMin, cMax):
                order.append(matrix[rMin][c])

            rMin += 1

            if not (rMin < rMax and cMin < cMax):
                break

            # Right
            for r in range(rMin, rMax):
                order.append(matrix[r][cMax-1])

            cMax -= 1

            if not (rMin < rMax and cMin < cMax):
                break

            # Bottom
            for c in range(cMax-1, cMin-1, -1):
                order.append(matrix[rMax-1][c])

            rMax -= 1

            if not (rMin < rMax and cMin < cMax):
                break

            # Left
            for r in range(rMax-1, rMin-1, -1):
                order.append(matrix[r][cMin])

            cMin += 1

        return order

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

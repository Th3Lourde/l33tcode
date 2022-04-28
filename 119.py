class Solution:
    def getRow(self, rowIndex):
        rows = []
        idx = 0

        while idx <= rowIndex:
            new_row = []

            for i in range(idx+1):
                if i == 0 or i == idx:
                    new_row.append(1)
                else:
                    new_row.append(rows[-1][i-1]+rows[-1][i])

            rows.append(new_row)

            idx += 1

        return rows[-1]

print(Solution().getRow(8))

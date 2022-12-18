'''
Each number is the sum of the two numbers directly
above it.

The only exception is the first and last, which are ones

The number of cols in each row is equal to the number of rows.
'''

class Solution:
    def generate(self, numRows):
        ans = []

        for rowNum in range(1, numRows+1):
            row = []
            for col in range(rowNum):
                if col == 0 or col == rowNum-1:
                    row.append(1)
                else:
                    row.append(ans[-1][col-1]+ans[-1][col])

            ans.append(row)

        return ans


print(Solution().generate(1))

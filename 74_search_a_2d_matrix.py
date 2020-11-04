'''
Write an efficient algo that searches
for a value in a square matrix.

So we use bin search to select a row,
then bin search to select a col

if we are between row i, row j, where i < j:

Looking for a row x ∋ targ ∈ [x[0], x[-1]]

Create mid-row

if targ < mid-row[0]:
    bottom = mid-row

elif targ > mid-row[-1]:
    top = mid-row + 1

Let's see how well that works




'''

class Solution:
    def searchMatrix(self, matrix, target):
        ans = False

        if len(matrix) == 0 or len(matrix[0]) == 0: return False

        top = 0
        bottom = len(matrix)-1

        # Find the correct row
        while top < bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                bottom = mid
                break

            elif target < matrix[mid][0]:
                bottom = mid

            elif target > matrix[mid][-1]:
                top = mid+1

        if not(matrix[bottom][0] <= target <= matrix[bottom][-1]):
            return ans

        # Find the correct column
        row = matrix[bottom]

        lo = 0
        hi = len(row)-1

        while lo < hi:
            mid = (lo + hi) // 2

            if target == row[mid]:
                hi = mid
                break

            elif target > row[mid]:
                lo = mid + 1

            elif target < row[mid]:
                hi = mid

        return matrix[bottom][hi] == target


if __name__ == '__main__':
    s = Solution()

    matrix = [
        [1,2,3,5],
        [6,7,8,9],
        [10,11,16,20],
        [23,30,34,50],
    ]

    print(s.searchMatrix(matrix, 13))

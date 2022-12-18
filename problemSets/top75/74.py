'''
Write an efficient algo that searches for a value target in an m x n integer matrix.
This matrix has the following properties:

- Integers in each row are sorted from left to right
- The first integer of each row is greater than the last
integer of the previous row


So one way we could do this is to put all of the values
in a single arr and perform binary search


Another way is to have a modified binary search algorithm

0(log(rows) + log(cols))

search for rows:
- Pick a row, if arr[0] <= target <= arr[-1], pick the row, else look up/down

'''

class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        # 1 find row
        u = 0
        d = rows-1

        while u < d:
            m = (u+d)//2

            if target > matrix[m][-1]:
                u = m + 1
            else:
                d = m

        l = 0
        r = cols-1

        while l < r:
            m = (l+r)//2

            if target > matrix[u][m]:
                l = m + 1
            else:
                r = m


        return matrix[u][l] == target


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 30))

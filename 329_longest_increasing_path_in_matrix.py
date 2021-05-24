class Solution:
    def longestIncreasingPath(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def itr(row, col):
            if dp[row][col] > -1:
                return dp[row][col]

            maxPathLength = 1

            for newRow, newCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= newRow < rows and 0 <= newCol < cols and matrix[newRow][newCol] > matrix[row][col]:
                    maxPathLength = max(maxPathLength, itr(newRow, newCol)+1)

            dp[row][col] = maxPathLength

            return dp[row][col]

        ans = 0

        for row in range(rows):
            for col in range(cols):
                ans = max(ans, itr(row, col))

        return ans

s = Solution()

print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) # 4
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])) # 4
print(s.longestIncreasingPath([[1]])) # 1

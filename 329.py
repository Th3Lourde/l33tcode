class Solution:
    def longestIncreasingPath(self, matrix):
        dp = {}
        longestPath = float('-inf')
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            l = 1

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[r][c] < matrix[nr][nc]:
                        l = max(l, dfs(nr,nc)+1)

            dp[(r,c)] = l
            return dp[(r,c)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                longestPath = max(longestPath, dfs(row, col))

        return longestPath

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(Solution().longestIncreasingPath([[1]]))

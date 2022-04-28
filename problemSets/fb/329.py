'''
loop through each element
perform a dfs, r
'''

class Solution:
    def longestIncreasingPath(self, matrix):
        longestPath = 0
        dp = {}

        def dfs(row, col, seen):
            if (row, col) in dp:
                return dp[(row, col)]

            path = 1

            for nr, nc in [(row+1,col), (row-1,col), (row, col+1), (row, col-1)]:
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                    if (nr, nc) not in seen and matrix[nr][nc] > matrix[row][col]:
                        seen.add((nr, nc))
                        longest_sub_path = dfs(nr, nc, seen)
                        path = max(path, longest_sub_path+1)
                        seen.remove((nr, nc))

            dp[(row, col)] = path
            return path

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                longestPath = max(longestPath, dfs(r,c, set({(r,c)})))

        print(dp)

        return longestPath

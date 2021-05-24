'''
Grid is: m x n
m = 3, n = 7
 21 15 10
0000631
7654321
1111111
'''

class Solution:
    def uniquePaths(self, m, n):
        dp = [ [0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][-1] = 1

        for i in range(n):
            dp[-1][i] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]


print(Solution().uniquePaths(2, 2))

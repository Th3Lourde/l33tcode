class Solution:
    def climbStairs(self, n):
        dp = [0 for _ in range(max(2,n))]

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]

print(Solution().climbStairs(3))

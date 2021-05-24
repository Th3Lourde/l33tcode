class Solution:
    def numTilings(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        dp = [0 for _ in range(n+1)]

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n+1):
            dp[i] = 2*dp[i-1]+dp[i-3]

        return dp[n]%(10**9 + 7)

s = Solution()

print(s.numTilings(1))
print(s.numTilings(2))
print(s.numTilings(3))

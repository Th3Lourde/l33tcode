
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        dp = [0 for _ in range(amount+1)]

        for i in range(amount+1):
            minCoinsRequired = float('inf')

            for coin in coins:
                if (i-coin) == 0:
                    minCoinsRequired = 1

                elif (i - coin) > 0 and dp[i-coin] != 0:
                    minCoinsRequired = min(minCoinsRequired, dp[i-coin]+1)

            dp[i] = minCoinsRequired

        if dp[amount] != float('inf'):
            return dp[amount]

        return -1

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([2,3], 6))
print(Solution().coinChange([1], 0))

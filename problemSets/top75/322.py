class Solution:
    def coinChange(self, coins, amount):
        dp = {}

        def itr(target):
            if target == 0:
                return 0

            if target in dp:
                return dp[target]

            resp = float('inf')

            for coin in coins:
                if (target - coin) >= 0:

                    resp = min(resp, itr(target-coin)+1)


            dp[target] = resp

            return dp[target]

        resp = itr(amount)

        if resp == 0:
            return 0

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]



print(Solution().coinChange([2,5,7], 11))
print(Solution().coinChange([1,2], 0))
print(Solution().coinChange([2], 3))

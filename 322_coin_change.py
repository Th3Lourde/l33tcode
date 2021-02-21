class Solution:
    def coinChange_1(self, coins, amount):
        dp = [float('inf') for _ in range(amount+1)]

        def itr(distance):
            if distance < 0:  return -1
            if distance == 0: return 0

            if dp[distance] != float('inf'):
                return dp[distance]

            minVal = float('inf')

            for c in coins:
                z = itr(distance-c)

                if z >= 0 and z+1 < minVal:
                    minVal = z+1

            if minVal == float('inf'):
                dp[distance] = -1
            else:
                dp[distance] = minVal

            return dp[distance]

        return itr(amount)

    # top down
    def coinChange_2(self, coins, amount):
        dp = [None for _ in range(amount+1)]
        dp[0] = 0

        def itr(n):
            if n < 0: return -1
            if n == 0: return 0

            if dp[n] != None: return dp[n]

            lowest = -1

            for coin in coins:
                req = itr(n-coin)

                if req != -1:
                    if lowest == -1:
                        lowest = req+1

                    elif req+1 < lowest:
                        lowest = req+1

            dp[n] = lowest
            return dp[n]

        itr(amount)
        return dp[amount]

    # bottom up
    def coinChange(self, coins, amount):
        dp = [None for _ in range(amount+1)]
        dp[0] = 0

        for n in range(1, amount+1):
            lowest = -1

            for c in coins:
                if n-c >= 0 and dp[n-c] != None:
                    if lowest == -1 and dp[n-c] != -1:
                        lowest = dp[n-c] + 1
                    elif lowest != -1 and dp[n-c] != -1 and dp[n-c]+1 < lowest:
                        lowest = dp[n-c] + 1

            dp[n] = lowest

        return dp[amount]



if __name__ == '__main__':
    s = Solution()
    print(s.coinChange( [1,2,5], 11))
    print(s.coinChange( [2], 3))
    print(s.coinChange( [1], 0))
    print(s.coinChange( [1], 0))
    print(s.coinChange( [186,419,83,408], 6249))

class Solution:

    def numSquaresRec(self, n):
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        def helper(num):
            if num in dp:
                return dp[num]
            i = 1
            dp[num] = num
            while i*i <= num:
                dp[num] = min(dp[num], helper(num - (i*i)) + 1)
                i += 1
                
            return dp[num]

        return helper(n)


    # Bottom-Up
    # Requires more calculations so not
    # as good
    def numSquaresItr(self, n):
        dp = [float('inf')] * (n+1)
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - (j*j)] + 1)
                j += 1
        return dp[n]

if __name__ == '__main__':
    s = Solution()

    print(s.numSquares(7))
    print(s.numSquares(9))
    print(s.numSquares(11))

    print(s.numSquares(12))

    print(s.numSquares(13))
    print(s.numSquares(18))
    print(s.numSquares(43))

    print(s.numSquares(172))
    print(s.numSquares(169))

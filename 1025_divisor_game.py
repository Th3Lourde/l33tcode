'''
TC: 0(n!)
SP: 0(n)
'''


class Solution:
    def divisorGame(self, n):
        dp = [False for _ in range(n+1)]

        if n == 1: return False

        dp[2] = True

        def getOpts(v):
            ans = []
            for i in range(1, v):
                if v % i == 0:
                    ans.append(i)
            return ans

        for i in range(n+1):
            # 1) Get options
            opts = getOpts(i)

            # 2) If one of the options maps to F → put T.
            dp[i] = False
            for opt in opts:
                if i-opt > 0 and dp[i-opt] == False:
                    dp[i] = True
                    break
        print(dp)
        return dp[n]

if __name__ == '__main__':
    s = Solution()

    print(s.divisorGame(5))
    print(s.divisorGame(7))
    print(s.divisorGame(8))

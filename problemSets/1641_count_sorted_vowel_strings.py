class Solution:
    # backtracking, works, is slow.
    # can also build the string
    def countVowelStrings_1(self, n):
        ans = [0]

        def itr(idx, s, solSet, ans):
            if s == 0:
                ans[0] += 1

            # print("idx: {}, s: {}, solSet: {}, ans: {}".format(idx, s, solSet, ans))

            if idx >= len(solSet) or s == 0:
                return

            for i in range(idx, len(solSet)):
                itr(i, s-1, solSet, ans)

        solSet = ["a","e","i","o","u"]

        itr(0, n, solSet, ans)

        return ans[0]

    # dp: top-down
    def countVowelStrings_2(self, n):
        dp = {}
        ans = [0]

        def itr(idx, s, solSet, ans, dp):
            if idx >= len(solSet) or s < 0: return 0

            if s == 0: return 1

            if (idx, s) in dp:
                return dp[(idx,s)]

            dpAns = 0

            for i in range(idx, len(solSet)):
                dpAns += itr(i, s-1, solSet, ans, dp)

            dp[(idx,s)] = dpAns

            return dp[(idx,s)]

        solSet = ["a","e","i","o","u"]

        itr(0, n, solSet, ans, dp)

        return dp[(0,n)]

    # dp: bottom-up
    def countVowelStrings_3(self, n):
        dp = [[1 for _ in range(6)]] + [[0 for _ in range(6)] for _ in range(n)]

        for i in range(1, n+1):
            for j in range(1,6):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[n][5]

    # dp: bottom-up with improved memory complexity
    def countVowelStrings(self, n):
        dp = [1 for _ in range(6)]

        for i in range(1, n+1):
            t = [0 for _ in range(6)]
            for j in range(1,6):
                t[j] = t[j-1] + dp[j]
            dp = list(t)

        return dp[5]




if __name__ == '__main__':
    s = Solution()
    print(s.countVowelStrings(33))

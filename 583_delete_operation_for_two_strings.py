class Solution:
    # Top-Down
    def minDistance_1(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i,j):
            if (i,j) not in memo:
                # Out of bounds
                if i == len(word1) or j == len(word2):
                    ans = len(word1) - i + len(word2) - j
                # Equal
                elif word1[i] == word2[j]:
                    ans = dp(i+1,j+1)
                else:
                    ans = 1 + min(dp(i+1, j), dp(i, j+1))

                memo[i,j] = ans

            return memo[i,j]

        return dp(0,0)

    def minDistance(self, w1, w2):
        M, N = len(w1), len(w2)

        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for i in range(M):
            dp[i][-1] = M-i

        for j in range(N):
            dp[-1][j] = N-j

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

s = Solution()

print(s.minDistance("dinitrophenylhydrazine","acetylphenylhydrazine"))

print(s.minDistance("sea", "eat"))
print(s.minDistance("leetcode", "etco"))
print(s.minDistance("a", "a"))
print(s.minDistance("ba", "ab"))

'''
leetcode
      ^

etco
   ^



'''

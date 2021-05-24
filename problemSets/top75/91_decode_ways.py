class Solution:
    def numDecodings(self, s):
        dp = [0 for _ in range(len(s))]

        if len(s) == 1:
            if "1" <= s <= "9":
                return 1
            return 0

        if len(s) == 2:
            numDecode = 0
            if "1" <= s[0] <= "9" and "1" <= s[1] <= "9":
                numDecode += 1
            if "10" <= s <= "26":
                numDecode += 1
            return numDecode

        if "1" <= s[0] <= "9":
            dp[0] += 1

        if dp[0] == 1 and "1" <= s[1] <= "9":
            dp[1] += 1

        if "10" <= s[:2] <= "26":
            dp[1] += 1

        for i in range(2, len(s)):
            if "1" <= s[i] <= "9":
                dp[i] += dp[i-1]

            if "10" <= s[i-1:i+1] <= "26":
                dp[i] += dp[i-2]

        return dp[-1]

print(Solution().numDecodings("101022342342123346"))
print(Solution().numDecodings("2062315"))

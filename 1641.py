
class Solution:
    def countVowelStrings(self, n):
        seen = {}

        def dp(n,k):
            if n==1 or k==1:
                return k

            if (n,k) in seen:
                return seen[(n,k)]

            seen[(n,k)] = sum(dp(n-1,k) for k in range(1,k+1))

            return seen[(n,k)]

        return dp(n,5)

print(Solution().countVowelStrings(33))

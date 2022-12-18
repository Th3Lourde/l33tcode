'''
1

(2,5,0)


01234567
abbababa
  l
    r
'''

class Solution:
    def isValidPalindrome(self, s, k):
        cache = {}

        def dfs(l,r,t):
            if l >= r:
                return True

            if (l,r,t) in cache:
                return cache[(l,r,t)]

            resp = False

            if s[l] == s[r]:
                resp = dfs(l+1, r-1, t)
            elif s[l] != s[r] and t > 0:
                resp = dfs(l+1, r, t-1) or dfs(l, r-1, t-1)

            cache[(l,r,t)] = resp

            return cache[(l,r,t)]

        return dfs(0, len(s)-1, k)

print(Solution().isValidPalindrome("abcdeca", 2))
print(Solution().isValidPalindrome("abbazbaba", 1))

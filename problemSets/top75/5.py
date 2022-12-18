
'''
Given a string s, return the longest palindromic
substring in s

Ok so I'm guessing this is a two pointer problem.
But maybe not. Not sure how to do this w/out doing
guess and check. Pick an idx (or two) then start expanding
out until it is no longer a pali.


Ok so I was totally right, lol.

Not sure if there's actually a faster way.
Anyhoot let's implement
'''

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        resp = ""

        def helper(l,r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]

        for idx in range(len(s)):

            r1 = helper(idx, idx)

            if len(r1) > len(resp):
                resp = r1

            r2 = helper(idx, idx+1)

            if len(r2) > len(resp):
                resp = r2

        return resp

class Solution:
    def reverse(self, x):
        isNeg = False
        ans = 0

        if x < 0:
            isNeg = True
            x *= -1


        while x:
            # print(x)
            ones = x % 10

            ans = ans*10 + ones

            x = int(x // 10)


        if isNeg:
            ans *= -1

        if -2**31 <= ans <= 2**31-1:
            return ans

        return 0


print(Solution().reverse(-123))

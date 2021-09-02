'''
Given a string s, return the longest palindromic substring in s.

1:
Start with sliding window, find all of the largest palindromes

length: 3

01234
babad
  ---

What is the time complexity for each iteration?
len(str)-potentialPaliLength+1

Worst Case: how many iterations?

n-(n-1) + n-(n-2) + n-(n-3) + n-(n-4) + ... + n-(n-2)

Exponential TC
Constant    SC

So this is actually a valid solution, however I
think we could do better.

You can also start from the middle and work outwards,
kinda the opposite of the solution that I came up with.
'''

class Solution:
    def longestPalindrome(self, s):
        def longestPali(l,r,odd):
            pali = ""

            if odd:
                pali = s[l+1]

            while 0 <= l and r < len(s) and s[l] == s[r]:
                pali = s[l] + pali + s[r]
                l -= 1
                r += 1

            return pali

        resp = ""

        if len(s) <= 1:
            return s

        for i in range(len(s)):
            l1 = longestPali(i,i+1,False)
            l2 = ""

            if i > 0:
                l2 = longestPali(i-1,i+1,True)

            if len(l1) > len(resp) and len(l1) > len(l2):
                resp = l1
            elif len(l2) > len(resp) and len(l2) > len(l1):
                resp = l2

        return resp

print(Solution().longestPalindrome("babad")) #bab
print(Solution().longestPalindrome("cbbd")) #bb
print(Solution().longestPalindrome("a")) #a
print(Solution().longestPalindrome("")) #""
print(Solution().longestPalindrome("ac")) #""

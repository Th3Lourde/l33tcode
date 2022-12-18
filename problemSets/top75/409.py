'''
Given a string s which consists of lowercase or uppercase letters, return the length
of the longest palindrome that can be created using the characters in s.

create a dict, then depending how many times 2
'''

class Solution:
    def longestPalindrome(self, s):
        d = {}
        ans = 0

        for chr in s:
            if chr in d:
                d[chr] += 1
            else:
                d[chr] = 1

        # First pass to get all even powers
        for key in d:
            if d[key] // 2 > 0:
                ans += 2*(d[key]//2)

        # Second pass to get the middle term
        for key in d:
            if d[key] % 2 == 1:
                ans += 1
                break

        return ans


print(Solution().longestPalindrome("ccc"))

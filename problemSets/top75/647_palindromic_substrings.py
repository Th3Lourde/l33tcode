'''
Given a string s, return the number of palindromic substrings in it.

Loop through each character, test to see if that character is the center
of an even or an odd pali

palis = "a","a","aa","aaa", "a", "aa"

"aaa"
   ^
  ^^


'''
class Solution:
    def countSubstrings(self, s):
        palis = 0

        def countPalis(l,r):
            palis = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                palis += 1
                r += 1
                l -= 1

            return palis

        for i in range(len(s)):
            palis += 1 + countPalis(i-1, i) + countPalis(i-1, i+1)

        return palis

print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))

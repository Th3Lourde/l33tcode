'''
A string is a pali if, after converting all upper to lower
and removing all non-alphanumeric chrs, it reads the same forwards
as backwards.

Return if s is pali.

Ok so one step for removing chrs we don't care about
one step for checking if it is a string.

loop through s, create a list that is the .lower() of the chrs
in s, only include if a-z, A-Z, can use regex, ascii values, or
dict lookup. I'll use ascii

'''

class Solution:
    def isPalindrome(self, s):
        chrs = set("")
        trimmedWord = []

        # Trim
        for chr in s:
            if 65 <= ord(chr) <= 90 or 97 <= ord(chr) <= 122 or 48 <= ord(chr) <= 57:
                trimmedWord.append(chr.lower())

        l = 0
        r = len(trimmedWord)-1

        while l != r and l < len(trimmedWord) and r >= 0:
            if trimmedWord[l] != trimmedWord[r]:
                return False

            l += 1
            r -= 1

        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

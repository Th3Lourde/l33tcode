'''
Given string, return if the string is a pali given:
constraint --> remove at most on chr



'''

class Solution:
    def validPalindrome(self, s):
        def isPalindrome(test_str):
            l = 0
            r = len(test_str)-1

            while l < r:
                if test_str[l] != test_str[r]:
                    return False

                l += 1
                r -= 1

            return True

        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                # del l or del r
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])

            l += 1
            r -= 1

        return True

print(Solution().validPalindrome("dcbc"))
print(Solution().validPalindrome("abc"))
print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome("aba"))

class Solution:
    def validPalindrome(self, s):
        l = 0
        r = len(s)-1

        def isPalindome(str):
            print(str)
            l = 0
            r = len(str)-1

            while l < r:
                if str[l] != str[r]:
                    return False

                l += 1
                r -= 1

            return True


        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindome(s[l+1:r+1]) or isPalindome(s[l:r])

        return True

print(Solution().validPalindrome("deeeee"))
print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome("abc"))
print(Solution().validPalindrome("dabca"))

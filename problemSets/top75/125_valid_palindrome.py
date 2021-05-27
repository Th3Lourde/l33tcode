class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s)-1

        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1

            if l == len(s):
                break

            while r > 0 and not s[r].isalnum():
                r -= 1

            if r == -1:
                break

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

print(Solution().isPalindrome("abba"))
print(Solution().isPalindrome("aba"))
print(Solution().isPalindrome("aabaa"))
print(Solution().isPalindrome(""))
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("0P"))

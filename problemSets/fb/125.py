class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s)-1

        while l < r:
            while s[l].isalnum() == False and l < r:
                l += 1

            while s[r].isalnum() == False and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                # print("s[l]: {} | s[r]: {}".format(s[l], s[r]))
                return False

            l += 1
            r -= 1

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(""))
print(Solution().isPalindrome("a"))
print(Solution().isPalindrome("ab"))
print(Solution().isPalindrome("aa"))
print(Solution().isPalindrome("aba"))

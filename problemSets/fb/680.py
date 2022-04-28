'''

abbca
'''

class Solution:
    def validPalindrome(self, s):
        l = 0
        r = len(s)-1
        stack = []
        canReset = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # If we have already put something on the stack
                if canReset == False:
                    # If we have already used what was on the stack
                    if stack == []:
                        return False

                    # Use what is on the stack
                    l, r = stack.pop()

                else:
                    # Put something on the stack
                    stack.append((l+1, r))
                    r -= 1
                    canReset = False

        return True

print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome("abba"))
print(Solution().validPalindrome("abcba"))
print(Solution().validPalindrome("abdvvba"))
print(Solution().validPalindrome("abdvvba"))
print(Solution().validPalindrome("abdevvba")) # False
print(Solution().validPalindrome("12345")) # False
print(Solution().validPalindrome("abc")) # False
print(Solution().validPalindrome("abac")) # False
print(Solution().validPalindrome("caba")) # False
print(Solution().validPalindrome("")) # False

'''
Given an integer x, return true if x in a palindrome
integer.

So get the one from x and add it to a new number
then compare if the numbers are equal.

'''

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        tmpX = x
        newX = 0

        while tmpX:
            ones = tmpX - ((tmpX // 10) * 10)
            newX += ones
            newX *= 10
            tmpX //= 10

        newX //= 10

        # print(newX)
        # print(x)

        return newX == x

print(Solution().isPalindrome(121))

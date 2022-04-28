'''
Given a list of integers, where said list
represents a large multi-digit number,
increment the number by one.
'''

class Solution:
    def plusOne(self, digits):
        digit = 1
        i = len(digits)-1

        while i >= 0:
            digits[i] += digit

            if digits[i] <= 9:
                digit = 0
                break
            else:
                digits[i] = 0

            i -= 1

        if digit == 1:
            return [1] + digits

        return digits

print(Solution().plusOne([9,9,9]))

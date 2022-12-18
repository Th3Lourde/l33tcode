'''
12

ones = 2

resp = 32
'''

class Solution:
    def reverse(self, x):
        resp = 0
        isNeg = False

        if x < 0:
            isNeg = True
            x *= -1


        while x:
            # get ones
            ones = x % 10

            # add ones to resp, move nums left
            resp = resp*10 + ones

            x = int(x//10)

        if isNeg:
            resp *= -1

        if -2**31 <= resp <= 2**31-1:
            return resp

        return 0


print(Solution().reverse(120))
print(Solution().reverse(-123))

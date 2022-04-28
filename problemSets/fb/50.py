'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

So assuming we can't do this with the power function, hopefully we'll be
able to use the multiplication attribute

So what can n be?

n is an integer. N can be positive or negative or zero.

'''

class Solution:
    def myPow_1(self, x, n):
        ans = 1

        for _ in range(abs(n)):
            ans *= x

        if n < 0:
            ans = 1/ans

        return ans

    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)

        if n % 2 == 0:
            return lower*lower
        if n % 2 == 1:
            return lower*lower*x



print(Solution().myPow(0.00001,2147483647))

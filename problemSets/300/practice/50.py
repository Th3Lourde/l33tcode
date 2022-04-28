class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)

        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x



    def myPow_1(self, x, n):
        negPower = False

        if n < 0:
            negPower = True
            n = abs(n)

        num = 1

        for _ in range(n):
            num *= x

        if negPower:
            return 1/num

        return num

print(Solution().myPow(5,-2))

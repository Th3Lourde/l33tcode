'''
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
'''

class Solution:

    def __init__(self):
        self.dp = []

    def tribonacci(self, n):
        self.dp = [0,1,1] + [-1 for i in range(n-1)]

        def findTrib(n):
            if self.dp[n] < 0:
                self.dp[n] = findTrib(n-1)+findTrib(n-2)+findTrib(n-3)
            return self.dp[n]

        return findTrib(n)




    def tribonacci_1(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

if __name__ == '__main__':
    s = Solution()

    print(s.tribonacci(4))
    print(s.tribonacci(25))

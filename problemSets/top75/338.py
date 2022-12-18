'''
Given an integer n, return an array ans
of length n + 1 such that for each element
ans[i] is the number of ones in the representation of i

0 | 0
1 | 1
2 | 10
3 | 11
4 | 100
5 | 101
6 | 110

Even --> number / 2
Odd --> (number-1)/2 + 1

'''

class Solution:
    def countBits(self, n):
        dp = [0,1,1]

        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        elif n == 2:
            return [0,1,1]

        for num in range(3, n+1):
            if num % 2 == 0:
                dp.append(dp[int(num/2)])
            else:
                dp.append(dp[int((num-1)/2)]+1)

        return dp

print(Solution().countBits(5))

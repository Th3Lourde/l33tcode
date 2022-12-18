class Solution:
    def hammingWeight(self, n):
        ones = 0

        while n:
            if n % 2 == 1:
                ones += 1

            n = n // 10

        return ones

print(Solution().hammingWeight(11111111111111111111111111111101))

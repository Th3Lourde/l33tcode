class Solution:
    def hammingWeight(self, n):
        ans = 0

        while n:
            ans += n&1
            n >>= 1

        return ans

print(Solution().hammingWeight(1))

a = 21

bin(a)
a >>= 1
bin(a&1)

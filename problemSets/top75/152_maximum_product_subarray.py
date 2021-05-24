class Solution:
    def maxProduct(self, nums):
        prefix = nums
        suffix = nums[::-1]

        for i in range(1, len(nums)):
            if prefix[i-1] != 0:
                prefix[i] *= prefix[i-1]

            if suffix[i-1] != 0:
                suffix[i] *= suffix[i-1]

        return max(prefix + suffix)

s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([-2,-3,-1]))
print(s.maxProduct([-3,-1,-1]))
print(s.maxProduct([3,-1,4]))
print(s.maxProduct([2,-5,-2,-4,3])) # 24

'''
[-2,1,-3,4,-1,2,1,-5,4]
                     ^

sum = 5
'''

class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]

        localSum = float('-inf')

        for n in nums:
            if localSum < 0:
                localSum = n
            else:
                localSum += n

            maxSum = max(maxSum, localSum)

        return maxSum

s = Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([-1]))

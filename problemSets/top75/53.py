'''
Given an integer array, find the contigious subarray
which has the largest sum. Return its sum

Ok so we have a sum and a number.

If the number + the sum < 0, set sum to zero
If the number + the sum > 0, add number to sum.
'''

class Solution:
    def maxSubArray(self, nums):
        maxSum = max(nums)
        currentSum = 0

        for num in nums:
            if num + currentSum > 0:
                currentSum += num
                maxSum = max(maxSum, currentSum)
            else:
                currentSum = 0


        return maxSum

print(Solution().maxSubArray([-1]))

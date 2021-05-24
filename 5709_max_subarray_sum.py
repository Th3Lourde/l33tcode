'''
Given array of positive integers: nums
Return maxPossible sum of ascending subarray in nums


'''

class Solution:
    def maxAscendingSum(self, nums):
        ans = max(nums)

        for i in range(len(nums)):
            subSum = nums[i]

            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    subSum += nums[j]
                else:
                    break

            if subSum > ans:
                ans = subSum

        return ans

s = Solution()

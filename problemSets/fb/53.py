'''
[-2,1,-3,4,-1,2,1,-5,4]
                     ^

    local_sum = max(element, local_sum+element)

    sum = max(local_sum, sum)

local_sum = 1
sum = 6
'''

class Solution:
    def maxSubArray(self, nums):
        sum = max(nums)
        local_sum = nums[0]

        for idx in range(1, len(nums)):
            local_sum = max(nums[idx], local_sum+nums[idx])
            sum = max(sum, local_sum)

        return sum


print(Solution().maxSubArray([-1,-2,-3]))
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

'''
[2,7,9,3,1]

Maximize value,
you can't rob houses
that are situated next to
each other

dp[i] = max(dp[i-2], dp[i-3])
'''

class Solution:
    def rob(self, nums):
        maxHit = 0

        for i in range(len(nums)):
            loot1 = 0

            if i - 2 >= 0:
                loot1 = nums[i-2]

            loot2 = 0

            if i - 3 >= 0:
                loot2 = nums[i-3]

            nums[i] += max(loot1, loot2)

            maxHit = max(maxHit, nums[i])

        return maxHit


print(Solution().rob([1,2,3,1]))

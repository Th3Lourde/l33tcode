'''
rob houses along street

you can't rob two adjacent houses

so you either rob the house on your direct right,
or the house on over.

1,2,3,1
1|2|4


'''

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        money = [0]*len(nums)
        money[0] = nums[0]
        money[1] = nums[1]

        for i in range(2, len(nums)):
            if i == 2:
                money[i] = money[i-2] + nums[i]

            else:
                money[i] = max(money[i-2], money[i-3]) + nums[i]

        return max(money)

print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([1,2,3,1]))

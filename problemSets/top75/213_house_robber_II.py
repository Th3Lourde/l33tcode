class Solution:
    def rob(self, nums):
        dp = [0 for _ in range(len(nums))]
        maxHit = 0

        if len(nums) < 3:
            return max(nums)

        # Skip house at end
        for i in range(len(nums)-1):
            profit1 = 0

            if i - 2 >= 0:
                profit1 = dp[i-2]

            profit2 = 0

            if i - 3 >= 0:
                profit2 = dp[i-3]

            dp[i] = max(profit1, profit2) + nums[i]

            maxHit = max(maxHit, dp[i])

        print(dp)

        dp = [0 for _ in range(len(nums))]

        # Skip house at beginning
        for i in range(len(nums)):
            profit1 = 0

            if i - 2 > 0:
                profit1 = dp[i-2]

            profit2 = 0

            if i - 3 > 0:
                profit2 = dp[i-3]

            dp[i] = max(profit1, profit2) + nums[i]

            maxHit = max(maxHit, dp[i])

        return maxHit

print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([0]))
print(Solution().rob([1]))
print(Solution().rob([1,2,1,1]))
print(Solution().rob([4,1,2,7,5,3,1]))

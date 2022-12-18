
class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        dp = {target:1}

        def itr(num):
            if num in dp:
                return dp[num]

            ways = 0

            for idx in range(len(nums)):
                if num+nums[idx] <= target:
                    ways += itr(num+nums[idx])

            dp[num] = ways
            return dp[num]

        ans = 0

        for num in nums:
            ans += itr(num)

        return ans

print(Solution().combinationSum4([1,2,3], 4))
print(Solution().combinationSum4([9], 3))

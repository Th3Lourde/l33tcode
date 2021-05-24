'''
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

[1,2,3], target = 4
   ^


 0  1  2  3  4
[1, 1, 2, 4, 7]
             ^

'''

class Solution:
    def combinationSum4(self, nums, target):
        dp = [0 for _ in range(target+1)]
        dp[0] = 1

        for i in range(1, target+1):
            distinctSums = 0

            for n in nums:
                if i-n >= 0:
                    distinctSums += dp[i-n]

            dp[i] = distinctSums

        return dp[target]

print(Solution().combinationSum4([1,2,3], 4))

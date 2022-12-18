'''
ok so mis-understood the problem.

We can include values or ignore them.
However we can't change their order.


'''

import bisect

class Solution:
    def lengthOfLIS(self, nums):
        dp = []

        for n in nums:
            idx = bisect.bisect_left(dp, n)

            if idx == len(dp):
                dp.append(n)
            else:
                dp[idx] = n

        return len(dp)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([0,1,7,7,8,9,7,10,11]))

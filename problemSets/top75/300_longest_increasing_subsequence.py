'''
Given integer array nums,
return the length of the strictly
increasing subsequence.

 0  1 2 3 4 5  6   7
[10,9,2,5,3,7,101,18]
                   ^

dp: [ ]


Start at the back. Keep a sorted array of
elements that we have solved for.

Idea:
You need to consider all values that are
larger than the value that you are currently
located at.

'''

class Solution:
    def lengthOfLIS(self, arr):
        maxLIS = 1
        dp = [0 for _ in range(len(arr))]
        dp[-1] = 1

        for l in range(len(arr)-1,-1,-1):
            LIS = 1

            for r in range(l+1, len(arr)):
                if arr[l] < arr[r]:
                    LIS = max(LIS, dp[r]+1)

            dp[l] = LIS

            maxLIS = max(maxLIS, dp[l])


        return maxLIS

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))

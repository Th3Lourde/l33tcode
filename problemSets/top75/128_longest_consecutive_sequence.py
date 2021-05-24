'''
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

[100,4,200,1,3,2]
  ^

memo = {
    100 : 0
    4 :   0
    200 : 0
    3 :   0
    2 :   0
}

top-down makes most sense
'''

class Solution:
    def longestConsecutive(self, nums):
        memo = {}

        for n in nums:
            memo[n] = 0

        def topDown(n):
            if n not in memo:
                return 0

            if memo[n] != 0:
                return memo[n]

            memo[n] = 1 + topDown(n+1)

            return memo[n]

        maxConsecutive = 0

        for n in nums:
            maxConsecutive = max(maxConsecutive, topDown(n))

        return maxConsecutive

print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive([]))

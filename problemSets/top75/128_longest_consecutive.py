'''
[100,4,200,1,3,2]
           ^

topDown(1)
    topDown(2)
        topDown(3)
            topDown(4)
            return 1

        return 2
    return 3
return 4

{
    1:4,
    2:3,
    3:2,
    4:1,
    100:1,
    200:1
}

'''

class Solution:
    def longestConsecutive(self, nums):

        if not nums:
            return 0

        memo = {}

        for n in nums:
            memo[n] = 0

        def topDown(val):
            if val not in memo:
                return 0
            elif memo[val] != 0:
                return memo[val]

            longest = 1

            if val+1 in memo:
                longest = max(longest, topDown(val+1)+1)

            memo[val] = longest
            return memo[val]

        longestRun = 1

        for n in nums:
            if memo[n] != 0:
                continue

            longestRun = max(longestRun, topDown(n))

        return longestRun

print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

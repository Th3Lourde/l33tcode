'''
Given a non-empty array, that contains only positive integers,
find if the array can be partitioned into two subsets
s.t. the sum of the elements in both subsets are equal.

So find the sum of the whole list, then find all subsets.
As we find all subsets, have a running sum, which represents
the sum of the remaining elements. If the running sum ever
equals the sum we have, return True

[1,5,5,11] | 22

0, [1,5,5,11]
1, [5,5,11]
5, [1,5,11]
5, [1,5,11]
11, [1,5,5]

itr(runningSum, opts)
'''

class Solution:
    def canPartition(self, nums):
        totalSum = sum(nums)
        cache = {}

        def backtrack(runningSum, opts):
            if runningSum == totalSum-runningSum:
                return True

            if runningSum in cache:
                return cache[runningSum]

            resp = False

            for idx, opt in enumerate(opts):
                if backtrack(runningSum+opt, opts[:idx]+opts[idx+1:]):
                    resp = True
                    break

            cache[runningSum] = resp
            return cache[runningSum]

        return backtrack(0, nums)

print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartition([1,2,3,4,5]))

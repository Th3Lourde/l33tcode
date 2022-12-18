'''
Given an array nums containing n distinct numbers
in the range [0,n], return the only number in the range
that is missing from the array.

sum([0,n]) == (n)(n+1)/2

sum the nums in nums and return the diff b/c that is the number
that is missing.
'''

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        targetSum = int(n*(n+1)/2)
        actualSum = sum(nums)

        missing = targetSum-actualSum

        return missing

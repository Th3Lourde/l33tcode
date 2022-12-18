'''
Given an non-empty array.

All but one elements appears twice
One element appears once

Find the element that appears once. All but one elements appear twice

Well we can sum the elements,

This is bit manipulation. God fucking dammit.
I hate bit manipulation, fuck this.
'''

class Solution:
    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans ^= num

        return ans

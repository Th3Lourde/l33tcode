'''
Given an array nums of size n, return the majory element.

The majority element is the element that appears more than n/2 times
'''

class Solution:
    def majorityElement(self, nums):
        majCount = len(nums)/2
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

            if d[num] >= majCount:
                return num

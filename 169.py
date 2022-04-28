'''
Given an array nums of size n,
return the majority element

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums):
        freq = {}
        n = len(nums)

        for _, num in enumerate(nums):
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

            if freq[num] > n / 2:
                return num

print(Solution().majorityElement([2,2,3]))

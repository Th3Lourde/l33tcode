'''
Given an array, rotate the array to the right by k steps, where k
is non negative

Oh this is just an array, we are good to go.

newIdx = (idx+1)%len(nums)?
'''

class Solution:
    def rotate(self, nums, k):
        n = len(nums)

        idxToVal = {}

        for idx in range(n):
            idxToVal[idx] = nums[idx]

        for idx in range(n):
            newIdx = (idx+k)%n
            nums[newIdx] = idxToVal[idx]

        return nums

print(Solution().rotate([1,2,3,4,5,6,7],3))

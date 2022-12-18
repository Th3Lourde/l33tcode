'''
Given an integer array nums,
move all 0's to the end of it while maintain the relative order of the non-zero elements

do in place.

Ok so modified bubble-sort. Loop through list, whenever you see
a zero, bubble the zero to the end of the list.
'''

class Solution:
    def moveZeroes(self, nums):
        l = 0
        n = len(nums)

        while l < n:
            if nums[l] == 0:
                # bubble to the right
                t = l
                while t + 1 < n:
                    nums[t], nums[t+1] = nums[t+1], nums[t]
                    t += 1

                n -=1
                l -= 1
            l += 1

        return nums

print(Solution().moveZeroes([0,0,1]))
print(Solution().moveZeroes([0]))
print(Solution().moveZeroes([0,1,0,3,12]))

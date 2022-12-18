'''
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers

Ok so sort the list.

Then have two pointers that move through the list in an 0(n^2) manner

binary search to look for target, can increase index or lower index if need be
to get closer.

maybe create new list that doesn't include the two idxs b/c simpler logic

[-4,-1,1,2]

'''

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l < r:

                if nums[i] + nums[l] + nums[r] == target:
                    return target

                elif abs(target-closest) > abs(target - (nums[i] + nums[l] + nums[r])):
                    closest = nums[i] + nums[l] + nums[r]

                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return closest

print(Solution().threeSumClosest([0,0,0], 1))
print(Solution().threeSumClosest([-1,2,1,-4], 0))
print(Solution().threeSumClosest([-1,2,1,-4], 1))

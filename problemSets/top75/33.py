'''
Search in a rotated sorted array

We are given an array that is sorted in ascending order.

The array is also rotated. Execute a binary search on such
an array.

Ok so here is what we do:
We have the left side of the array and the right side of the array.
If the left side is sorted, then check if our target is in the bounds
if it is, then go left. If it isn't, go right.

It is given that at least one of the subarrays is sorted. Base you actions
upon the subarray that is sorted.
'''

class Solution:
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            m = (l+r)//2

            if nums[l] <= nums[m]:
                # Sorted, can check bounds
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m+1

            else:
                # The right subarry is sorted, check there

                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m-1

        if nums[l] == target:
            return l

        elif nums[r] == target:
            return r

        return -1

print(Solution().search([4,5,6,7,0,1], 1))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))

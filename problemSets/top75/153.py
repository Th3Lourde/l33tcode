'''
Find min in rotated sorted array

ok so linear solution: min(arr)

log(n) solution, implement binary search,
looking for the smallest element
'''

class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums)

        if nums[-1] < nums[-2]:
            return nums[-1]

        l = 0
        r = len(nums)-1
        minVal = float('inf')

        while l < r:
            m = (l+r)//2

            if nums[l] < nums[m]:
                # lhs is sorted
                # smallest value is nums[l]
                minVal = min(minVal, nums[l])

                # keep looking
                l = m+1

            else:
                # must be true that
                # nums[m] < nums[r]
                minVal = min(minVal, nums[m])

                # keep looking
                r = m

        return minVal

print(Solution().findMin([3,2,1]))
print(Solution().findMin([1,2]))
print(Solution().findMin([0,1,2,3]))

print(Solution().findMin([2,3,4,5,1]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([11,13,15,17]))

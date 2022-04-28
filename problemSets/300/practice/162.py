'''
peak element: element greater than neighbors


[1,5,3,4,5,6,7,8,9]
           b
                 e

          

'''

class Solution:
    def findPeakElement(self, nums):
        beg, end = 0, len(nums) - 1
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] < nums[mid + 1]:
                beg = mid + 1
            else:
                end = mid

        return end

print(Solution().findPeakElement([1,5,3,4,5,6,7,8,9]))

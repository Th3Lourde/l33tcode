class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1

        if nums[-1] < target:
            return len(nums)

        while l < r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            elif nums[m] <= target:
                l = m+1
            else:
                r = m

        return l


print(Solution().searchInsert([1,3,5,6], 0))

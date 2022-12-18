



class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2

            if nums[m] < target:
                l = m+1
            else:
                r = m

        if nums[l] != target:
            return -1

        return l

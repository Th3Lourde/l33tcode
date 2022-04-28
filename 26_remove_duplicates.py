'''

'''

class Solution:
    def removeDuplicates(self, nums):
        i = 0

        while i < len(nums):
            if i != 0:
                if nums[i-1] == nums[i]:
                    del nums[i]
                else:
                    i += 1
            else:
                i += 1

        return len(nums)

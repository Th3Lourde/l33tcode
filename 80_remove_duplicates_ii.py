'''
Given an array sorted in increasing order

Each element can occur up to two times.
Since we can only have 0(c) memory,

Keep track of if we need to shuffle the memory via a constant.
When we need to update the arr, remove the extra elements.

We are in python. So just del[idx]


'''

class Solution:
    def removeDuplicates(self, nums):
        count = 0
        term = 0
        i = 0

        while i < len(nums):
            if count == 0 or nums[i] != term:
                term = nums[i]
                count = 1
                i += 1

            elif nums[i] == term and count < 2:
                count += 1
                i += 1

            elif nums[i] == term and count >= 2:
                while i < len(nums) and nums[i] == term:
                    del nums[i]

                count = 0

        return len(nums)

print(Solution().removeDuplicates([1,1,1,2,2,3]))
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))

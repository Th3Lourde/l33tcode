'''
Given an integer array nums which is sorted in ascending order
All elements are unique.
Given an integer k

return the kth missing number starting from the leftmost num on arr

k = 4

[4,7,10]
     ^

- check right, if next term is consecutive, do nothing
- else:
|--> if nums[i+1]-nums[i] < k
    |--> k -= nums[i+1]-nums[i]
|--> else:
    return nums[i]+k?

'''

class Solution:
    def missingElement(self, nums, k):
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                diff = nums[i+1] - nums[i] - 1

                if k > diff:
                    k -= diff
                else:
                    return nums[i]+k

        return nums[-1]+k

'''
There is an integer array nums sorted in non-decreasing order
(might not be composed of distinct values)

The array is rotated

Just return if the target is in nums
I'm guessing the goal of this is to
have a run-time of 0(log(n))

Sorting: 0(n log(n))
We could remove duplicates 0(n), then binary search 0(log(n)) --> 0(n)
Or we could do some modified binary search, which would be between linear
and log time. Worse case could be linear?

If l == r, l+=1

[2,5,6,0,0,1,2]
   l         r

So just add in the += condition else we are good

target: 0
'''

class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        if nums[0] == target or nums[-1] == target:
            return True

        l = 0
        r = len(nums)-1

        # seen = set({nums[l], nums[r]})

        while l < r:
            while nums[l] == nums[r] and l < r:
                l += 1

            while nums[l] in seen and l < r:
                l += 1

            while nums[r] in seen and l < r:
                r -= 1

            if nums[l] == target or nums[r] == target:
                return True

            m = (l+r)//2

            seen.add(nums[m])

            if nums[m] == target:
                return True

            if nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m+1

            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m

        return False

print(Solution().search([0,0,1,1,2,0], 2))
print(Solution().search([2,5,6,0,0,1,2], 0))
print(Solution().search([2,5,6,0,0,1,2], 3))

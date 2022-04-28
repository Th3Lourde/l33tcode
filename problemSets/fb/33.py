'''
Search in Rotated Sorted Array

Nums is an arr[int]
nums has been sorted in ascending order and was
then rotated.

That being true, given a number target, search nums
to see if target is in the nums.

If it isn't, return -1

Ok so this is going to be a variant on binary search.

[4,5,6,7,0,1,2]
 l     m     r

Figure out which part of the array is sorted

if l <= m and m > target:
    r = m

if m <= r and r > target:
    l = m+1


target = 5
'''

class Solution:
    def search(self, nums, target):
        ans = -1

        l = 0
        r = len(nums)-1

        if nums[l] == target: return l
        if nums[r] == target: return r

        while l < r:
            m = (l+r)//2
            # print("L:{} R:{}".format(nums[l], nums[r]))

            if nums[m] == target:
                return m

            elif nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m

                else:
                    # pick the part of the list it can be
                    l = m+1

            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m

        return ans

print(Solution().search([4,5,6,7,0,1,2], 2))

'''
targ: 2

 0 1 2 3 4 5 6
[4,5,6,7,0,1,2]
         l m r

'''

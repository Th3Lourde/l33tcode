class Solution:
    def sortColors(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        idx = 0

        while l < n and nums[l] == 0:
            l += 1

        while r >= 0 and nums[r] == 2:
            r -= 1

        if l >= n or r <= 0:
            return nums

        while idx <= r:
            # print(idx)
            if idx < l or nums[idx] == 1:
                idx += 1
                continue

            elif nums[idx] == 0:
                nums[l], nums[idx] = nums[idx], nums[l]

            elif nums[idx] == 2:
                nums[r], nums[idx] = nums[idx], nums[r]

            while l < n and nums[l] == 0:
                l += 1

            while r >= 0 and nums[r] == 2:
                r -= 1

        return nums

print(Solution().sortColors([2,0,1]))

'''
[1,0,2]
 l
    r
 i


'''

print(Solution().sortColors([2,0,2,1,1,0]))

print(Solution().sortColors([0,0,0,0,1,1,1,2,2,2,2,1,1,1,2,0,2,1,1,0]))



print(Solution().sortColors([0,0,0,0,0,0,0,0,0]))
print(Solution().sortColors([2,2,2,2,2]))

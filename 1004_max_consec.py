'''
Start with left, right pointer
while the number of zeroes is low enough, increment the right pointer
while the number of zeroes is too high decrement the left pointer
every time we increment the right pointer compare to the max length

k=2
1,1,1,0,0,1,1,1,1,1,1
l
r


'''

class Solution:
    def longestOnes(self, nums, k):
        resp = 0
        l = 0
        r = 0

        while r < len(nums):
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

            while k >= 0 and r < len(nums):
                if nums[r] == 0:
                    k -= 1

                if k >= 0:
                    resp = max(resp, r-l+1)

                r += 1

        return resp


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

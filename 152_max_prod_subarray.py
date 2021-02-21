
class Solution:
    def maxProductO(self, nums) -> int:
        nums2 = nums[::-1]

        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            nums2[i] *= nums2[i-1] or 1

        return max(nums + nums2)

    def maxProduct2(self, nums) -> int:
        r = nums[0]
        r_min = r
        r_max = r

        for i in range(1, len(nums)):

            if nums[i] < 0:
                tmp = r_max
                r_max = r_min
                r_min = tmp


            r_max = max(nums[i], r_max*nums[i])
            r_min = min(nums[i], r_min*nums[i])


            r = max(r, r_max)

        return r

    def maxProduct(self, nums):
        res = max(nums)
        curMax,curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax,curMin = 1, 1
                continue

            tmp = curMax * n

            curMax = max(n, curMax*n, curMin*n)
            curMin = min(n, tmp, curMin*n)
            res = max(curMax, curMin, res)

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))

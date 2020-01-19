


class Solution:
    def maxProduct(self, nums) -> int:
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


if __name__ == '__main__':
    # n = [2,3,-2]
    # n = [2,3,-2,4]
    n = [-2,3,-4]

    s = Solution()
    r = s.maxProduct(n)
    print(r)


    # n = [2,3,-2]
    # n = [2,3,-2,4]
    n = [-2,3,-4]

    r = s.maxProduct2(n)
    print(r)

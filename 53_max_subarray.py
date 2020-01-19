
class Solution:
    def maxSubArray(self, nums) -> int:
        s = nums[0]

        for i in range(1, len(nums)):
            if (nums[i-1]+nums[i]) > nums[i]:
                nums[i] = nums[i-1]+nums[i]

            s = max(s, nums[i])

        return s


if __name__ == '__main__':
    n = [-2,1,-3,4,-1,2,1,-5,4]

    s = Solution()

    r = s.maxSubArray(n)
    print(r)

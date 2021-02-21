
class Solution:
    def maxSubArrayO(self, nums) -> int:
        s = nums[0]

        for i in range(1, len(nums)):
            if (nums[i-1]+nums[i]) > nums[i]:
                nums[i] = nums[i-1]+nums[i]

            s = max(s, nums[i])

        return s

        # kadane's algorithm
    def maxSubArray(self, nums):
        ans = float('-inf')
        current_sum = 0

        for num in nums:
            if current_sum + num > num:
                current_sum = current_sum + num
            else:
                current_sum = num

            if current_sum > ans:
                ans = current_sum

        return ans

if __name__ == '__main__':
    n = [-2,1,-3,4,-1,2,1,-5,4]

    s = Solution()

    r = s.maxSubArray(n)
    print(r)

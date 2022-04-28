class Solution:
    def subarraySum(self, nums, k):
        running_sum = 0
        sum_to_freq = {0:1}
        ans = 0

        for num in nums:
            running_sum += num

            if running_sum - k in sum_to_freq:
                ans += sum_to_freq[running_sum - k]

            if running_sum in sum_to_freq:
                sum_to_freq[running_sum] += 1
            else:
                sum_to_freq[running_sum] = 1

        return ans


print(Solution().subarraySum([-1, -1, 1], 0))
print(Solution().subarraySum([1], 0))
print(Solution().subarraySum([1,1,1], 2))
print(Solution().subarraySum([1,2,3], 0))
print(Solution().subarraySum([1,2,3], 3))

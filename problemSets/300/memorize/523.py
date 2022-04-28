class Solution:
    def checkSubarraySum(self, nums, k):
        prev_sums = {0:-1}
        run = 0

        for idx in range(len(nums)):
            run += nums[idx]
            run = run % k

            if run in prev_sums:
                if (idx-prev_sums[run]>1):
                    return True
            else:
                prev_sums[run] = idx

        return False

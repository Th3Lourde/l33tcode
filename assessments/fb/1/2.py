'''
ans is in the middle, not touching either edges (D)
ans is the whole list
ans is left to center (D)
ans is right to center (D)

'''

class Solution:
    def maxSubArrayLen(self, nums, k):
        d = {0: [-1]}
        ans = 0
        local_sum = 0

        for idx, num in enumerate(nums):
            local_sum += num

            if local_sum-k in d:
                subArrLen = idx - min(d[local_sum-k])
                ans = max(ans, subArrLen)

            if local_sum in d:
                d[local_sum].append(idx)
            else:
                d[local_sum] = [idx]

        return ans

print(Solution().maxSubArrayLen([1,1,1,0,0,1,-1,-1,1], 3))
print(Solution().maxSubArrayLen([-2,-1,2,1], 1))

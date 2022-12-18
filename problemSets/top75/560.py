









class Solution:
    def subarraySum(self, nums, k):
        d = {0:[-1]}
        s = 0
        ans = 0

        for idx, n in enumerate(nums):
            s += n

            if s-k in d:
                ans += len(d[s-k])

            if s in d:
                d[s].append(idx)
            else:
                d[s] = [idx]

        return ans

print(Solution().subarraySum([1,1,1],2))
print(Solution().subarraySum([1,2,3],3))

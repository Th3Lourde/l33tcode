class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        resp = max(nums)
        minP = None
        maxP = None

        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                minP = None
                maxP = None
                continue

            elif not minP and not maxP:
                minP, maxP = nums[i], nums[i]

            else:
                minP, maxP = min(nums[i], nums[i]*minP, nums[i]*maxP), max(nums[i], nums[i]*maxP, nums[i]*minP)

            # print("{}|{}|{}|{}".format(nums[i],resp, minP, maxP))

            resp = max(resp, minP, maxP)

        return resp

print(Solution().maxProduct([10,10,10,0,-1,9,8,-1,9,8,-1]))
print(Solution().maxProduct([-1,2,3,-2,4]))
print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))

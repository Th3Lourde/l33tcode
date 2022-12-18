class Solution:
    def sortedSquares(self, nums):
        firstPos = 0
        n = len(nums)

        while firstPos < n and nums[firstPos] < 0:
            firstPos += 1

        if firstPos == n:
            ans = []

            for num in reversed(nums):
                ans.append(num**2)

            return ans


        l = firstPos-1
        r = firstPos
        n = len(nums)
        ans = []

        while nums[l] < 0 and r < n:
            if abs(nums[l]) < nums[r]:
                ans.append(nums[l]**2)
                l -= 1
            else:
                ans.append(nums[r]**2)
                r += 1

        while nums[l] < 0:
            ans.append(nums[l]**2)
            l -= 1

        while r < n:
            ans.append(nums[r]**2)
            r += 1

        return ans

print(Solution().sortedSquares([-3,-2,-1]))
print(Solution().sortedSquares([-5,-3,-2,-1]))

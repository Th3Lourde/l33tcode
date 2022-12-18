

class Solution:
    def canJump(self, nums):
        if len(nums) == 1: return True

        n, numJumps = len(nums), 1

        for idx in range(n-2, 0, -1):
            if nums[idx] >= numJumps:
                numJumps = 1
            else:
                numJumps += 1

        return nums[0] >= numJumps

print(Solution().canJump([0]))
print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))

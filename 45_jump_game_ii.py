from collections import deque
class Solution:
    # Ok this is the brute-force solution
    # not sure time complexity, but it is top-down dp
    # Let's implement bfs
    def jump_1(self, nums):
        dp = {}

        def howManyJumps(idx):
            if idx >= len(nums)-1:
                return 0

            if idx in dp:
                return dp[idx]

            jumps = float('inf')

            for jumpDistance in range(1, nums[idx]+1):
                jumps = min(jumps, 1+howManyJumps(idx+jumpDistance))

            dp[idx] = jumps

            return dp[idx]

        return howManyJumps(0)

    # Too slow, but correct
    def jump_2(self, nums):
        # (idx, jump)
        q = deque({(0,0)})
        n = len(nums)-1

        while q:
            idx, jumps = q.pop()

            if idx >= n:
                return jumps

            for nextJump in range(1, nums[idx]+1):
                q.appendleft((idx+nextJump, jumps+1))

    def jump(self, nums):
        # Start from rhs, move backwards
        # Pick the furthest element left and continue
        # This works b/c we know there is a path accross
        jumps = 0
        idx = len(nums)-1

        while idx > 0:
            for newIdx in range(0, idx):
                if newIdx+nums[newIdx] >= idx:
                    idx = newIdx
                    jumps += 1
                    break


        return jumps


print(Solution().jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))

print(Solution().jump([0]))
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))

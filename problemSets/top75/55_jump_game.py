'''
   T T T T
[2,3,1,1,4]
   ^
 3
[3,2,1,0,4]
 F F F F T
'''

class Solution:
    def canJump(self, nums):

        if len(nums) <= 1:
            return True

        minJump = 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= minJump or i == len(nums)-1:
                minJump = 1
            else:
                minJump += 1

        return minJump == 1

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,0,0,4]))
print(Solution().canJump([2,0,0]))

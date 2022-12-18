'''
Given a circular integer array nums
return the next greater number for
every element in nums.

if it doesn't exist, return set it to be -1

0(n^2) look right for every element

res = [2,3,4,-1,4]

[1,2,3,4,3]
         ^

[4]

'''

class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        resp = [-1] * len(nums)

        for _ in range(2):
            for i in range(len(nums)):
                while stack and (nums[stack[-1]] < nums[i]):
                    resp[stack.pop()] = nums[i]
                stack.append(i)

        return resp

print(Solution().nextGreaterElements([1,2,3,4,3]))
print(Solution().nextGreaterElements([1,2,1]))

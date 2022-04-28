'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

1) Create a set that contains all of the numbers and remove from set
as you loop through nums
2) Sum 1 --> n

1 + 2 + 3 + 4 + 5
15

13

sum - actual sum = missing number

len(nums)+1 = 5
 0 1 2 3
[3,0,1]
     ^

i = 2


'''

class Solution:
    def missingNumber(self, nums):
        expectedSum = 0
        i = 0

        while i < len(nums):
            expectedSum += i
            expectedSum -= nums[i]

            i += 1

        expectedSum += i

        return expectedSum

print(Solution().missingNumber([3,1,2]))

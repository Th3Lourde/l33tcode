'''
[-1,1,-1,1]

[1,1,-1,-1]

prefix:
[0,1,2,1,0]

So if the sum went from being -1 --> -1 we know that it was zero

if the sum went from 0 --> 0, we know it was zero

So it is looking like we cut one off from the length?

0) Map all 0's to -1's
1) Create a prefix sum
2) Create a dict where the key is the sum and the value is the index
3) Loop through list, idx's will be sorted, store the max diff-1
return max diff

Still doesn't work, make some tea, restroom, think
'''

class Solution:
    def findMaxLength(self, nums):
        if len(nums) < 2:
            return 0

        maxLen = 0
        summation = 0
        d = {0:-1}

        for idx, num in enumerate(nums):
            # Update summation
            if num == 0:
                summation += -1
            else:
                summation += 1

            # Check if summation already exists
            # update maxLen if it does
            if summation in d:
                maxLen = max(maxLen, idx-d[summation])
            else:
                d[summation] = idx

        return maxLen

print(Solution().findMaxLength([1,0]))
print(Solution().findMaxLength([1,0,1,1,0,1,1,1,0,0,0]))
print(Solution().findMaxLength([0,1,0,1,1,0,1])) #6

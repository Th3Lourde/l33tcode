'''
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Brute force,
Out of all of the zeroes that we have, perform all permutations of interting k ones.
For each permutation, find the max number of consecutive ones.

What if we compress this?
Sum the ones and sum the zeros (treat them as negative ones)

[1,1,1,0,0,0,1,1,1,1,0]
[3,-3,4,-1] k = 2

Let's have runs. Start on a positive value and see how far right
we can go. Every time we are greeted with a negative value, we either
cross it or end.

Go left to right. Every time we see a positive value, make a call to
a function that returns the longest ones we can get if we treat the one
that we are at as the left side of the run.

[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
     l
                   r

maxRun = 8
lPtr = 0
rPtr = 0
localRun = 7
swapsLeft = 1

'''

class Solution:
    def longestOnes(self, nums, k):
        if 1 not in nums:
            return k

        if 0 not in nums:
            return len(nums)

        maxRun = 0

        lPtr = 0
        rPtr = 0
        localRun = 0
        swapsLeft = k

        while rPtr < len(nums):

            # Undo swaps
            while swapsLeft == 0:
                if nums[lPtr] == 0:
                    swapsLeft += 1

                lPtr += 1
                localRun -= 1

            while rPtr < len(nums):
                if nums[rPtr] == 0:
                    if swapsLeft == 0:
                        maxRun = max(maxRun, localRun)
                        break

                    swapsLeft -= 1

                localRun += 1
                rPtr += 1

                maxRun = max(maxRun, localRun)


        return maxRun

print(Solution().longestOnes([1,1,1,1,1], 0))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))

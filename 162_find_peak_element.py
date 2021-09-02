'''
A peak element is an element that is strictly greater than its
neighbors.

Given an integer array, find a peak element and return its index.
If the array contains multiple peaks, return the index of any of the peaks

You must write an algorithm that runs in 0(log n) time.

So then we need to use binary search, but binary search only works when
the array is sorted. So how can we do this?

We know that there must be a peak element

[1,2,3,1]
 ^   m ^

If odd pick middle element, if even pick the larger of the two?

 0 1 2 3 4 5 6
[1,2,1,3,5,6,4]
         l r
           m
           r

l = m + 1 iff arr[m] < arr[m+1]
r = m iff arr[m] >= arr[m+1]

'''

class Solution:
    def findPeakElement(self, nums):
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2

            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m

        return r


Solution().findPeakElement([1,2,3,4])

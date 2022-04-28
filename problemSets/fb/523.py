'''
Given an integer array nums
and an integer k

return t/f, depending on whether or not nums
has a continuous subarray of size at least two
that is a multiple of k.

[23,2,4,6,7], k = 6

So when we care about a multiple of k, we are talking
about modulus.

So we should keep a running sum going, but should mod it
every time we add to it.

The current sum doesn't need to be a mod of k, however we
are interested if the total sum has gone up by a multiple of k.

Thus, if our sum has mod x, we are curious to know if we have seen
x before, or if our sum has been mod x before.


'''

class Solution:
    def checkSubarraySum(self, nums, k):
        ...

print(Solution().checkSubarraySum( [1,2,12], 6))
print(Solution().checkSubarraySum( [23,2,4,6,7],  6 )) # True
print(Solution().checkSubarraySum( [23,2,6,4,5,5,7], 10)) # True
print(Solution().checkSubarraySum( [23,2,6,4,7], 6)) # True
print(Solution().checkSubarraySum( [23,2,6,4,7], 13)) # False
print(Solution().checkSubarraySum( [23,2,6,0,0], 13)) # True

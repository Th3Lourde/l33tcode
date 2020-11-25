'''
Given an array of integers (nums)
And a threshold (threshold)

∃ x ∋ every element in nums divided by
x, summed, is ≤ threshold.

Find the smallest value of x possible.

Each result of division is rounded to the
nearest integer ≥ element.

7/3 = 3
10/2= 5




'''
import math

class Solution:

    def calcSum(self, arr, m):
        resp = 0

        for e in arr:
            resp += math.ceil(e/m)

        return resp


    def smallestDivisor(self, nums, threshold):
        l, h = 1, max(nums)

        while l < h:
            m = (l+h)//2

            if self.calcSum(nums, m) > threshold:
                l = m + 1

            else:
                h = m

        return l

if __name__ == '__main__':
    s = Solution()

    print(s.smallestDivisor([1,2,5,9], 6) == 5)
    print(s.smallestDivisor([2,3,5,7,11], 11) == 3)
    print(s.smallestDivisor([19], 5) == 4)

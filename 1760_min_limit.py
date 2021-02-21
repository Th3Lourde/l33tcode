'''
Binary search works here even though the
elements aren't sorted.

That's because we aren't looking for a certain
element, we are looking for a valid parameter.

That parameter being the max value.

Take a guess at what the max value might be, figure
out how many operations it takes to get there.

If too high, go left, if we have room, go right.

The number of operations is (a - 1) / mid

where a is the element and mid is our target
'''

class Solution:
    def minimumSize(self, nums, maxOperations):
        l = 1
        r = int(10E9)

        while l < r:
            m = (l+r)//2

            ops = sum((e-1)//m for e in nums)

            if ops > maxOperations:
                l = m+1
            else:
                r = m

        return l

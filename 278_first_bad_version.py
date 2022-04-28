'''
So we have a function called isBadVersion
We have n which represents version numbers.
isBadVersion(n) --> returns T/F.

Find the first n that returns true for isBadVersion

This is a binary search problem
'''

class Solution:
    def firstBadVersion(self, n):
        l = 0
        r = n

        if isBadVersion(l):
            return l

        while l < r:
            m = (l+r)//2

            if isBadVersion(m):
                r = m
            else:
                l = m+1

        return l

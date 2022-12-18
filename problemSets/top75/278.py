'''
Ok so you have a function that you can call that tells you
if something is a bad version or not

So we want to find the smallest bad version.




'''



class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n

        while l < r:
            m = (l+r)//2

            if isBadVersion(m):
                r = m
            else:
                l = m+1

        return l

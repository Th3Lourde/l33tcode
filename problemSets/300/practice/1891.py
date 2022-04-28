'''
Given int array ribbons
ribbons[i] represents length of ith ribbon

Goal is to obtain k ribbons that all have the
same positive integer length.

Seems like we care about the k-th largest number
We can also just sort ribbons

ribbons = [7,5,9], k = 4
'''

t = [1,2,3,4]

t[-3]

class Solution:
    def maxLength(self, ribbons, k):
        if sum(ribbons) < k:
            return 0

        l = 1
        r = sum(ribbons)
        ans = 0

        while l < r:
            m = (l+r) // 2

            cuts = 0

            for ribbon in ribbons:
                cuts += ribbon//m

            if cuts >= k:
                ans = max(ans, m)
                l = m+1
            else:
                r = m

        return ans

print(Solution().maxLength([9,7,5], 4))

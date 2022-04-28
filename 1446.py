'''
01234567
leetcode
    ^

maxP = 2

idx = 4
localP = 1

'''

class Solution:
    def maxPower(self, s):
        maxP = 1

        idx = 1
        localP = 1

        while idx < len(s):
            if s[idx-1] == s[idx]:
                localP += 1
            else:
                maxP = max(maxP, localP)
                localP = 1

            idx += 1

        return max(maxP, localP)

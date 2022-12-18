'''
Initialize dict with keys a-z.
And values of zero.

for s += 1 to the val
for t -= 1 to the val

loop through all vals, should all be 0.
If aren't, return False
'''

class Solution:
    def isAnagram(self, s, t):
        d = {}
        chrs = 'abcdefghijklmnopqrstuvwxyz'

        for chr in chrs:
            d[chr] = 0

        for chr in s:
            d[chr] += 1

        for chr in t:
            d[chr] -= 1

        for key in d:
            if d[key] != 0:
                return False

        return True

print(Solution().isAnagram("anagram", "nagaramz"))

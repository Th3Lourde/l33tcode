class Solution:
    def arraySign(self, nums):
        negs = 0

        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                negs += 1

        if negs % 2 == 1:
            return -1

        return 1

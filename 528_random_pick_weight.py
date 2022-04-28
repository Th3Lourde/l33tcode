'''
Given w, list of int, which represents
weights of each index
probability of picking index i is:
w[i] / sum(w)


1,3

'''
import random

class Solution:
    def __init__(self, w):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w

    def pickIndex(self):
        target = random.randint(1,self.w[-1])
        l, r = 0, len(self.w)-1

        while l < r:
            m = (l+r)//2

            if target <= self.w[m]:
                r = m
            else:
                l = m+1

        return l


s = Solution([1,3])
s.pickIndex()

    # def __init__(self, w):
    #     self.n = sum(w)
    #     self.idxToElement = [-1 for _ in range(self.n)]
    #     idx = 0
    #
    #     for i in range(len(w)):
    #         for _ in range(w[i]):
    #             self.idxToElement[idx] = i
    #             idx += 1
    #
    #     self.idx = 0
    #     print(self.idxToElement)
    #
    # def pickIndex(self):
    #     self.idx += 1
    #
    #     if self.idx >= self.n:
    #         self.idx = 0
    #
    #     return self.idxToElement[self.idx]
